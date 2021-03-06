import shutil
import os
from typing import Iterable, Set


def _delete(files: Iterable[str]):
    for path in files:
        shutil.rmtree(
            path,
            onerror=(lambda func, path, exc_info: print(path, exc_info))
        )


def _search(directory: str) -> Set[str]:
    """ Рекурсивный поиск  """
    out: Set[str] = set()
    try:
        objects = os.listdir(directory)
        for i in objects:
            path = os.path.join(directory, i)
            if not os.path.isdir(path):
                continue
            if i == "__pycache__":
                print(path)
                out.add(path)
            else:
                out.update(_search(path))
    except PermissionError as e:
        print(e)
    return out


def clean(directory: str, autoagree: bool = False):
    _to_delete = _search(directory)
    if _to_delete:
        if autoagree:
            _delete(_to_delete)
        if not autoagree:
            print(
                f"found {len(_to_delete)} folders.",
                "Delete? (y/n): ", end=""
                )
            confirmation = input()
            if confirmation.strip().lower() == "y":
                _delete(_to_delete)
                print("Completed.")
            else:
                print("Canceled.")
    else:
        print("Not finded __pycache__ folders.")
