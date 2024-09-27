import requests

# Webex Bot Token and Room ID
WEBEX_BOT_TOKEN = 'your_webex_bot_token'
WEBEX_ROOM_ID = 'your_webex_room_id'  # Room where the bot will post messages

# Function to send message to Webex
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

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent to Webex successfully.")
    else:
        print(f"Error sending message to Webex: {response.status_code}, {response.text}")
