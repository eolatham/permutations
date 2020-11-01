# Permutations

This repo holds my solution to the problem of generating string permutations in Python using purely built-in syntax.

## Brainstorming Process

### [brainstorm.py](brainstorm.py)

1. I started by solving the simplest non-trivial case (`n=2`).
2. I kept stepping up (by incrementing `n`) until the pattern became clear.

In this exercise, I discovered that the [natural solution](#General-Solution) is recursive.

#### Example Thought Process

```
Let s = abc.
- n = 3
- output length = 3! = 3*2*1 = 6

Group permutations based on starting character:
- Permutations starting with a:
  - a + x for x in the permutations of the other characters in s (bc)
    - a + bc = abc
    - a + cb = acb
- Perms starting with b:
  - b + x for x in the permutations of the other characters in s (ac)
    - b + ac = bac
    - b + ca = bca
- Perms starting with c:
  - c + x for x in the permutations of the other characters in s (ab)
    - c + ab = cab
    - c + ba = cba

With all groups combined into one set, you have the answer:
{abc, acb, bac, bca, cab, cba}
```

## General Solution

### [permutations.py](permutations.py)

This was surprisingly difficult to come up with prior to going through the brainstorming process, but after the brainstorming process, it was very easy.

This solution is also extremely slow, but that's the nature of the algorithm (factorial time!).

Nonetheless, permutations seem to pop up in many places.

I wonder what methods exist for improving it...
