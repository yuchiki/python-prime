"""数列ユーティリティモジュール."""

from typing import List


class InvalidArgument(Exception):
    """引数が不正なことを表すエラー."""


def prime_numbers(length: int) -> List[int]:
    """素数を小さい順にlength個並べたリストを返す.

    Args:
        length (int): 素数リストの長さ

    Returns:
        List[int]: 小さい方からlength個並んだ素数列

    Raises:
        InvalidArgument: 引数が負のとき.
    """
    pass
