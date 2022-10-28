"""数列ユーティリティモジュール."""

import math
from typing import List


class InvalidArgument(Exception):
    """引数が不正なときのエラー."""


def prime_numbers(max: int) -> List[int]:
    """max以下の昇順の素数列を返す.

    Args:
        max (int): 探索範囲の上限

    Returns:
        List[int]: max以下の昇順の素数列

    Examples:
    >>> prime_numbers(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> prime_numbers(-4)
    []
    """
    # 実装の読みやすさを考慮して naive な方法で生成する.
    # 高速さが求められるようになった場合、以下のエラストテネスの篩法を検討する.
    # https://ja.wikipedia.org/w/index.php?title=%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9&oldid=91234491

    return [num for num in range(1, max + 1) if is_prime(num)]


def is_prime(num: int) -> bool:
    """素数かどうかを判定する.

    Args:
        num (int): 判定される整数(1以上).

    Returns:
        bool: 入力値が素数かどうか

    Raises:
        InvalidArgument: 引数が0以下のとき

    Examples:
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(1)
    False
    >>> is_prime(0)
    Traceback (most recent call last):
        ...
    num_utility.InvalidArgument
    """
    if num <= 0:
        raise InvalidArgument()

    if num == 1:
        return False

    return all(num % i != 0 for i in range(2, math.floor(math.sqrt(num) + 1)))
