#!/usr/bin/env python3
"""This module contains the Test class for the file `utils.py`"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the class `GithubOrgClient`"""

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the method `org`"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
