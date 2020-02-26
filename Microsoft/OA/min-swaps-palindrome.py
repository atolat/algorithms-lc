from collections import defaultdict
from typing import Dict, List


def can_be_palindrome(i: str) -> bool:
    char_count: Dict[str, int] = defaultdict(int)
    for c in i:
        char_count[c] = char_count[c] + 1
    str_len: int = len(i)
    count_odd: int = 0
    for k, e in char_count.items():
        if e % 2 != 0:
            count_odd += 1

    if str_len % 2 == 0:
        return count_odd == 0
    else:
        return count_odd == 1


def compute_palindrome(i: str) -> str:
    char_count: Dict[str, int] = defaultdict(int)
    for c in i:
        char_count[c] = char_count[c] + 1

    res: str = ""
    middle: str = ""
    for c in i:
        if char_count[c] != 0:
            if char_count[c] == 1:
                middle = c
                char_count[c] -= 1
            else:
                res += c
                char_count[c] -= 2

    return res + middle + res[-1::-1]


def min_swaps_anagram(source: str, target: str) -> int:
    s_l: List[str] = list(source)
    t_l: List[str] = list(target)
    count: int = 0
    for i in range(0, len(s_l)):
        pos = s_l[i:].index(t_l[i])

        while 0 < pos:
            s_l[i + pos], s_l[i + pos - 1] = s_l[i + pos - 1], s_l[i + pos]
            count += 1
            pos -= 1

    return count


def min_swaps_palindrome(source: str) -> int:
    if not can_be_palindrome(source):
        return -1

    target = compute_palindrome(source)

    return min_swaps_anagram(source, target)