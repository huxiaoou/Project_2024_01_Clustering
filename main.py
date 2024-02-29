if __name__ == "__main__":
    import sys
    import pandas as pd
    from clustering import CDataReader, optimize_k_and_labels, optimize_with_center

    return_file_dir = r"E:\Deploy\Data\ForProjects\cta3\instruments_return"
    return_file_name = "instruments_return.csv.gz"
    bgn_date, end_date = sys.argv[1], sys.argv[2]
    min_cluster_n, max_cluster_n = (int(_) for _ in sys.argv[3].split(","))
    verbose = sys.argv[4].upper() in ["V", "VERBOSE"] if len(sys.argv) >= 5 else False

    # find best K
    range_k = range(min_cluster_n, max_cluster_n + 1)
    range_rs = range(10)
    data_reader = CDataReader(return_file_name, return_file_dir)
    df_ret_nom = data_reader.get_range(bgn_date, end_date, normalize=True).T
    k1, labels_nom = optimize_k_and_labels(df_ret_nom, range_k, range_rs, verbose)

    # with pre-specified centers
    pre_sec_center = [
        "AU.SHF", "CU.SHF", "NI.SHF", "RB.SHF", "J.DCE", "Y.DCE",
        "BU.SHF", "C.DCE", "CF.CZC", "SF.CZC", "L.DCE", "SR.CZC"
    ]
    centers = df_ret_nom.loc[pre_sec_center]  # shape = (k, n_features)
    labels_center = optimize_with_center(df_ret_nom, centers)

    # print
    df_sector = pd.DataFrame({
        "instrument": df_ret_nom.index,
        "sector_nom": labels_nom,
        "sector_cen": labels_center,
    })
    print(df_sector.sort_values("sector_nom"))
    print(df_sector.sort_values("sector_cen"))
