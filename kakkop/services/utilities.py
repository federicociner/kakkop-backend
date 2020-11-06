from typing import Any, Dict, List


def find_index(items: List[Dict], key: Any, value: Any) -> int:
    for index, d in enumerate(items):
        if d[key] == value:
            return index

    return -1
