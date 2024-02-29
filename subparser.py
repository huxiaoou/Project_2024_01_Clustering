import argparse


def fun_check(bgn: str):
    print(f"check {bgn}")
    return 0


def fun_view(date: str):
    print(f"view {date}")
    return 0
#

parser = argparse.ArgumentParser(description="A command line tool")

subparsers = parser.add_subparsers(title="subcommands", dest='switch')

parser_sub1 = subparsers.add_parser(name='check', help='check data')
parser_sub1.add_argument('-b', "--bgn", type=str, help='begin date')
parser_sub1.set_defaults(func=fun_check)

parser_sub2 = subparsers.add_parser(name='view', help='view data')
parser_sub2.add_argument('-d', "--date", type=str, help='trade date')
parser_sub2.set_defaults(func=fun_view)

args = parser.parse_args()
if args.switch == "check":
    fun_check(args.bgn)
elif args.switch == "view":
    fun_view(args.date)
else:
    # class SwitchError(ValueError):
    #     def __init__(self, switch: str):
    #         super().__init__()
    #         self.switch = switch
    #
    #     def __str__(self):
    #         return f"switch = {self.switch} is wrong."
    #
    #
    # raise SwitchError(args.switch)
    pass
