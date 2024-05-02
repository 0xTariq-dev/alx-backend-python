#!/usr/bin/env python3
"""This module contains a function sum_mixed_list which takes
a mixed list of integers and floats and returns their sum as a float"""

from typing import List, Union

intAndFloat = Union[int, float]


def sum_mixed_list(mxd_lst: List[intAndFloat]) -> float:
    """Returns the sum of a mixed list of intgers and floats"""
    return sum(mxd_lst)
