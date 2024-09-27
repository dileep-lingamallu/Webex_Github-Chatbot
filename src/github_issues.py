import requests
import logging
import os
from datetime import datetime, timedelta

# GitHub API Token and repository info (use environment variables for security)
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'repo_owner'  # e.g., 'octocat'
REPO_NAME = 'repo_name'  # e.g., 'Hello-World'

logging.basicConfig(filename='bot.log', level=logging.INFO)

# Function to get new issues from the GitHub repository with error handling
def get_new_issues(since_time):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {
        "since": since_time.isoformat(),  # Get issues created since this time
        "state": "open",  # Only fetch open issues
        "per_page": 100  # GitHub paginates results
    }

    issues = []
    try:
        logging.info("Fetching new issues from GitHub")
        page = 1
        while True:
            params['page'] = page
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()  # Will raise an error for bad responses
            new_issues = response.json()
            if not new_issues:
                break
            issues.extend(new_issues)
            page += 1
        logging.info(f"Retrieved {len(issues)} new issues.")
        return issues
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching issues from GitHub: {e}")
        return []
