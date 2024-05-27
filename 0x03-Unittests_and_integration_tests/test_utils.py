#!/usr/bin/env python3
"""This module contains the Test class for the file `utils.py`"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Any, Sequence, Dict


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


class TestGetJson(unittest.TestCase):
    """Test cases for the function `get_json`"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, res: Dict):
        """Test the function `get_json`"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = res
            self.assertEqual(get_json(url), res)
            mock_get.assert_called_once_with(url)
