#!/usr/bin/env python3
"""Type-annotated function safely_get_value"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
tOrNone = Union[T, None]
tOrAny = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any,
                     default: tOrNone = None) -> tOrAny:
    """Return the value of a key in a dictionary or the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
