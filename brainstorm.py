# STL
from typing import Set
from itertools import permutations

# LOCAL
from common import control, str_del


def perms0(s0: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 0
    that is equivalent to set("".join(x) for x in permutations(s0)).
    """
    p = set()
    n = len(s0)
    assert n == 0
    return {s0}


def perms1(s1: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 1
    that is equivalent to set("".join(x) for x in permutations(s1)).
    """
    p = set()
    n = len(s1)
    assert n == 1
    return {s1}


def perms2(s2: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 2
    that is equivalent to set("".join(x) for x in permutations(s2)).
    """
    p = set()
    n = len(s2)
    assert n == 2
    for i in range(n):
        for s1 in perms1(str_del(s2, i, n)):
            p.add(s2[i] + s1)
    return p


def perms3(s3: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 3
    that is equivalent to set("".join(x) for x in permutations(s3)).
    """
    p = set()
    n = len(s3)
    assert n == 3
    for i in range(n):
        for s2 in perms2(str_del(s3, i, n)):
            p.add(s3[i] + s2)
    return p


def perms4(s4: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 4
    that is equivalent to set("".join(x) for x in permutations(s4)).
    """
    p = set()
    n = len(s4)
    assert n == 4
    for i in range(n):
        for s3 in perms3(str_del(s4, i, n)):
            p.add(s4[i] + s3)
    return p


if __name__ == "__main__":
    function_map = {
        0: perms0,
        1: perms1,
        2: perms2,
        3: perms3,
        4: perms4,
    }
    test_data = ["", "a", "ab", "abc", "abcd"]
    for i in range(len(test_data)):
        result = function_map[i](test_data[i])
        print(
            f"perms{i}('{test_data[i]}') = {result}\n"
            f"length: {len(result)}\n"
            f"correct: {result == control(test_data[i])}\n",
        )
