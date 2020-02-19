import requests
import json


def get_repo_info(user_name='Sachin568'):
    output = []
    user_url = 'https://api.github.com/users/{}/repos'.format(user_name)
    res = requests.get(user_url)
    repos = json.loads(res.text)
    output.append('User: {}'.format(user_name))

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name)
            repo_info = requests.get(repo_url)
            repo_info_json = json.loads(repo_info.text)
            output.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_info_json)))
        for entry in get_repo_info():
            print(entry)
        return output
    except (Exception):
        return Exception

# print(get_repo_info(user_name="Sachin568"))
if __name__ == '__main__':
    get_repo_info()
    

    