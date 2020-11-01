# STL
from typing import Set
from itertools import permutations

# LOCAL
from common import str_del


def perms2(s2: str) -> Set[str]:
    """
    Return the set of permutations for a string of length 2
    that is equivalent to set("".join(x) for x in permutations(s2)).
    """
    assert len(s2) == 2
    p = {s2, s2[::-1]}
    assert p == set("".join(x) for x in permutations(s2))
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
    assert p == set("".join(x) for x in permutations(s3))
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
    assert p == set("".join(x) for x in permutations(s4))
    return p
