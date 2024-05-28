#!/usr/bin/env python3

FAKE_PAYLOAD = {
    "repos_url": "https://api.github.com/orgs/google/repos",
    'repos': [
        {
            "id": 7697149,
            "name": "episodes.dart",
            "private": False,
            "owner": {
                "login": "google",
                "id": 1342004,
            },
            "fork": False,
            "url": "https://api.github.com/repos/google/episodes.dart",
            "created_at": "2013-01-19T00:31:37Z",
            "updated_at": "2019-09-23T11:53:58Z",
            "has_issues": True,
            "forks": 22,
            "default_branch": "master",
        },
        {
            "id": 7776515,
            "name": "cpp-netlib",
            "private": False,
            "owner": {
                "login": "google",
                "id": 1342004,
            },
            "fork": True,
            "url": "https://api.github.com/repos/google/cpp-netlib",
            "created_at": "2013-01-23T14:45:32Z",
            "updated_at": "2019-11-15T02:26:31Z",
            "has_issues": False,
            "forks": 59,
            "default_branch": "master",
        }
    ]
}
