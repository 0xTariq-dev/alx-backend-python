#!/usr/bin/env python3
"""This module contains a function zoom_array"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Args:
        lst (Tuple): a tuple of values of any type
        factor (int, optional): a number by which the tuple will be zoomed.

    Returns:
        List: a list of values of any type
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
