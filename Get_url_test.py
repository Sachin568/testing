import unittest
from unittest import mock
from Get_url import get_repo_info


class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        """Testing to check for expected repositories"""
        expected = [
            "User: Sachin568",
            "Repo: Django Number of commits: 1",
            "Repo: embedded-projects Number of commits: 2",
            "Repo: helloworld Number of commits: 1",
            "Repo: Image-Processing Number of commits: 2",
            "Repo: IoT-automation Number of commits: 2",
            "Repo: Python_Repository Number of commits: 6",
            "Repo: testing Number of commits: 21",
            "Repo: Web-controlled-robot Number of commits: 2",
            "Repo: web-_programming Number of commits: 2",
        ]
        self.assertEqual(get_repo_info(), expected)

    # def test_bad_user_name(self):
    #     self.assertEqual(get_repo_info(), 'unable to fetch repos from user')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
