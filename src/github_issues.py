import requests
from datetime import datetime, timedelta

# GitHub API Token and repository info
GITHUB_TOKEN = 'your_github_token'
REPO_OWNER = 'repo_owner'  # e.g., 'octocat'
REPO_NAME = 'repo_name'  # e.g., 'Hello-World'

# Function to get new issues from the GitHub repository
def get_new_issues(since_time):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {
        "since": since_time.isoformat(),  # Get issues created since this time
        "state": "open"  # Only fetch open issues
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()  # List of issues
    else:
        print("Error fetching issues from GitHub:", response.status_code)
        return []
