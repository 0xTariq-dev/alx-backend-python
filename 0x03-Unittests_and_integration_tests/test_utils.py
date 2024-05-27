#!/usr/bin/env python3
"""This module contains the Test class for the file `utils.py`"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Any, Sequence, Union


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the function `access_nested_map`"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, n_map: Mapping, path: Sequence, res: Any):
        """Test the function `access_nested_map`"""
        self.assertEqual(access_nested_map(n_map, path), res)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, n_map: Mapping, path: Sequence,
                                         res: Any):
        """Test the function `access_nested_map`"""
        with self.assertRaises(res):
            access_nested_map(n_map, path)
