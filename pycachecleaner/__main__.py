import os
from .pycachecleaner import clean


if __name__ == "__main__":
    clean(os.getcwd())