#!/usr/bin/env python3
"""This module contains the Test class for the file `utils.py`"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict
from fixtures import TEST_PAYLOAD
from fake_payload import FAKE_PAYLOAD as FakePayload
from requests import HTTPError


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test the method `public_repos`"""
        test_payload = FakePayload

        mock_get_json.return_value = test_payload['repos']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload['repos_url']
            test_class = GithubOrgClient('google')
            self.assertEqual(
                test_class.public_repos(),
                ['episodes.dart', 'cpp-netlib']
                )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        (FakePayload['repos'][0], "bsd-3-clause", True),
        (FakePayload['repos'][1], "bsd-3-clause", False)
    ])
    def test_has_license(self, repo: Dict, key: str, res: bool) -> None:
        """Test the method `has_license`"""
        test_class = GithubOrgClient('google')
        self.assertEqual(test_class.has_license(repo, key), res)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the class `GithubOrgClient`"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up for the class `TestIntegrationGithubOrgClient`"""
        gh_org = GithubOrgClient('google')
        url, repos_url = gh_org.org['url'], gh_org.org['repos_url']

        route_payload = {
            f'{url}': cls.org_payload,
            f'{repos_url}': cls.repos_payload,
        }

        def side_effect(url: str) -> Dict:
            """Side effect for the `get_json` mock"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test the method `public_repos` """
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Test the method `has_license"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(license="apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down for the class `TestIntegrationGithubOrgClient`"""
        cls.get_patcher.stop()
