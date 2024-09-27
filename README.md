# Webex Chatbot for Summarizing GitHub Issues

This project is a Python-based Webex chatbot that summarizes GitHub issues using the OpenAI ChatGPT API and sends the summary to a specified Webex room daily.

## Project Structure

```
Webex_Chatbot_Project/
│
├── src/
│   ├── github_issues.py         # Script for fetching GitHub issues
│   ├── summarize_issues.py      # Script for summarizing issues using ChatGPT
│   ├── webex_message.py         # Script for sending summary to Webex
│   └── schedule_task.py         # Script for scheduling the entire process
│
└── README.md                    # Project instructions
```

## Prerequisites

1. **Python 3.x** installed.
2. Install the required Python packages:
   ```
   pip install requests schedule openai
   ```

3. **GitHub Token:** Create a GitHub API token with permissions to read issues.
   - You can generate a personal access token from your GitHub account settings.

4. **OpenAI API Key:** Obtain an API key from OpenAI to use the ChatGPT API.
   - Sign up at [OpenAI](https://beta.openai.com/signup/) and get your API key.

5. **Webex Bot Token:**
   - Go to [Webex Developer Portal](https://developer.webex.com/) and create a bot.
   - After creating the bot, you'll get a **Bot Access Token**. Save it for later.

6. **Webex Room ID:**
   - Use the Webex API to retrieve the room ID where the bot will post the summary.
   - Add the bot to the desired Webex room, then use the following script to get the room ID:
     ```python
     import requests
     WEBEX_BOT_TOKEN = 'your_webex_bot_token'
     def get_rooms():
         url = "https://webexapis.com/v1/rooms"
         headers = {
             "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
             "Content-Type": "application/json"
         }
         response = requests.get(url, headers=headers)
         if response.status_code == 200:
             rooms = response.json()['items']
             for room in rooms:
                 print(f"Room Name: {room['title']}, Room ID: {room['id']}")
         else:
             print(f"Failed to fetch rooms: {response.status_code}")
     get_rooms()
     ```

## Running the Project

1. Set your **GitHub token**, **OpenAI API key**, **Webex bot token**, and **Webex room ID** in the respective Python scripts.
2. Schedule the bot to run daily using `schedule_task.py`. You can customize the scheduling time if needed.
   ```
   python src/schedule_task.py
   ```
3. The bot will fetch GitHub issues from the last 24 hours, summarize them using ChatGPT, and send the summary to the Webex room at the scheduled time (9:00 AM by default).

## Customization

- You can modify the scripts to suit your needs, such as:
  - Fetching issues from multiple repositories.
  - Changing the formatting of the summary sent to Webex.
  - Adding error handling or logging.