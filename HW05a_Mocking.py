import unittest
from unittest import mock
from Get_url import get_repo_info
from unittest.mock import Mock, patch
import Get_url


class TestGetRepo(unittest.TestCase):
    @mock.patch("Get_url.get_repo_info")
    def test_get_repo(self, mock_fun):
        """Mocking request to get access every time"""
        expected = [
            "User: Sachin568",
            "Repo: Django Number of commits: 1",
            "Repo: embedded-projects Number of commits: 2",
            "Repo: helloworld Number of commits: 1",
            "Repo: Image-Processing Number of commits: 2",
            "Repo: IoT-automation Number of commits: 2",
            "Repo: Python_Repository Number of commits: 6",
            "Repo: testing Number of commits: 30",
            "Repo: Web-controlled-robot Number of commits: 2",
            "Repo: web-_programming Number of commits: 2",
        ]
        mock_fun.return_value = "Mocked successful"
        result = Get_url.get_repo_info()
        self.assertEqual(result, "Mocked successful")

        mock_fun.return_value = get_repo_info()
        result1 = Get_url.get_repo_info()

        self.assertEqual(result1, expected)
        self.assertNotEqual(result1, "unable to fetch repos from user")
        return (result, result1)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

