import requests
import logging
import os

# Webex Bot Token and Room ID (from environment variables)
WEBEX_BOT_TOKEN = os.getenv('WEBEX_BOT_TOKEN')
WEBEX_ROOM_ID = os.getenv('WEBEX_ROOM_ID')  # Room where the bot will post messages

logging.basicConfig(filename='webex_bot.log', level=logging.INFO)

# Function to send message to Webex with error handling
def send_message_to_webex(summary):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "roomId": WEBEX_ROOM_ID,
        "text": summary
    }

    try:
        logging.info("Sending message to Webex.")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()  # Raise error if request fails
        logging.info("Message sent to Webex successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending message to Webex: {e}")
