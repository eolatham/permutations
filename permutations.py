# STL
from typing import Set
from itertools import permutations

# LOCAL
from common import control, str_del


def perms(s: str) -> Set[str]:
    """
    Return the set of permutations for s that is
    equivalent to set("".join(x) for x in permutations(s)).
    """
    n = len(s)
    if n < 2:
        return {s}
    else:
        output = set()
        for i in range(n):
            for p in perms(str_del(s, i, n)):
                output.add(s[i] + p)
        return output


if __name__ == "__main__":
    for s in ["", "a", "ab", "abc", "abcd"]:
        result = perms(s)
        print(
            f"perms('{s}') = {result}\n"
            f"length: {len(result)}\n"
            f"correct: {result == control(s)}\n",
        )
