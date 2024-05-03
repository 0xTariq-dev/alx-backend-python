#!/usr/bin/env python3
"""This module contains the safe_first_element function"""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or None if empty"""
    if lst:
        return lst[0]
    else:
        return None
