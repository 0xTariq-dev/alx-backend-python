#!/usr/bin/env python3
"""This module contains function to_kv that takes a string k and an int v as
 arguments and returns a tuple. The first element of the tuple is the string k.
 the second element is the square of the int v and should be annotated
 as a float."""

from typing import Tuple, Union

num = Union[int, float]


def to_kv(k: str, v: num) -> Tuple[str, float]:
    """
    Args:
        k: str
        v: float or int
    Returns:
        Tuple[str, float]: a tuple containing the string k and the square of v
    """
    return (k, v ** 2)
