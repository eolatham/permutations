# STL
from typing import Set
from itertools import permutations


def control(s: str) -> Set[str]:
    return set("".join(x) for x in permutations(s))


def str_del(s: str, i: int, n: int) -> str:
    """
    Return a copy of the string s of length n
    with the ith character removed.
    """
    assert i > -1 and i < n
    if i == n - 1:
        return s[:i]
    else:
        return s[:i] + s[i + 1 :]
