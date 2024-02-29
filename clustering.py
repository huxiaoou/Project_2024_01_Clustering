import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


class CDataReader(object):
    def __init__(self, return_file_name: str, return_file_dir: str):
        self.return_file_name = return_file_name
        self.return_file_dir = return_file_dir
        self.return_df = pd.read_csv(self.return_file_path, dtype={"trade_date": str}).set_index("trade_date")

    @property
    def return_file_path(self) -> str:
        return os.path.join(self.return_file_dir, self.return_file_name)

    def get_range(self, bgn_date: str, end_date: str, normalize: bool, fillna_value: float = 0) -> pd.DataFrame:
        df = self.return_df.truncate(before=bgn_date, after=end_date).dropna(axis=1, how="all")
        if normalize:
            return ((df - df.mean()) / df.std()).fillna(fillna_value)
        return df.fillna(fillna_value)


def optimize_k_and_labels(data: pd.DataFrame, range_k: range, range_rs: range, verbose: bool = False) -> tuple[int, pd.Series]:
    silh_scores: dict[tuple[int, int], float] = {}
    labels: dict[tuple[int, int], pd.Series] = {}
    for k in range_k:
        for rs in range_rs:
            labels[k, rs] = KMeans(n_clusters=k, n_init="auto", random_state=rs).fit_predict(data)
            silh_scores[k, rs] = silhouette_score(data, labels[k, rs])
    score_srs = pd.Series(silh_scores)
    k, rs = score_srs.idxmax()
    n, size = data.shape
    print("=" * 24)
    if verbose:
        print(score_srs)
    print("-" * 24)
    print(f"size   of instruments = {n}")
    print(f"length of windows     = {size}")
    print(f"best K, Random State  = {k}, {rs}")
    print("=" * 24)
    return k, labels[k, rs]
