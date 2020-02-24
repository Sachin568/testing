import requests
import json


def get_repo_info():
    user_name, output = 'Sachin568', []
    user_url =requests.get(f'https://api.github.com/users/{user_name}/repos')
    repos = json.loads(user_url.text)
    output.append(f'User: {user_name}')

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch repos from user'

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = requests.get(f'https://api.github.com/repos/{user_name}/{repo_name}/commits')
            repo_info_json = json.loads(repo_url.text)
            output.append((f'Repo: {repo_name} Number of commits: {len(repo_info_json)}'))
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch commits from repo'
    return output
    

if __name__ == '__main__':
    for entry in get_repo_info():
        print(entry)




    