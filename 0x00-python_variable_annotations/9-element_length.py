#!/usr/bin/env python3
"""This module contains the function element_length"""

from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples containing the length of each element and the
    element itself"""
    return [(i, len(i)) for i in lst]
