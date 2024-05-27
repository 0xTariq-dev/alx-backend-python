#!/usr/bin/env python3
"""This module contains the Test class for the file `utils.py`"""

import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict


# @patch('client.get_json')
# @parameterized_class(('org_name', 'mock_get_json'), [
#     ('google', Mock()),
#     ('abc', Mock())
# ])
class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the class `GithubOrgClient`"""

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Dict) -> None:
        """Test the method `org`"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self) -> None:
        """Test the method `_public_repos_url`"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            test_class = GithubOrgClient('google')
            self.assertEqual(
                test_class._public_repos_url,
                "https://api.github.com/users/google/repos"
                )
