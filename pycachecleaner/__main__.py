import argparse
import os

from .pycachecleaner import clean


parser = argparse.ArgumentParser(description="delete __pycache__")
parser.add_argument(
    "dirs",
    metavar="D",
    type=str,
    nargs="*",
    help="an directories to clean"
)
parser.add_argument(
    "--auto",
    dest="auto",
    action="store_true",
    default=False,
    help="no confirmation",
)

args = parser.parse_args()


if __name__ == "__main__":
    if args.dirs:
        for i in args.dirs:
            if os.path.exists(i) and os.path.isdir(i):
                clean(i, autoagree=args.auto)
            elif not os.path.isdir(i):
                print(f"{repr(i)} not a directory")
            else:
                print(f"directory {repr(i)} not exists")
    else:
        clean(os.getcwd(), autoagree=args.auto)
