import schedule
import time
import logging
from datetime import datetime, timedelta
from github_issues import get_new_issues
from summarize_issues import summarize_issues
from webex_message import send_message_to_webex

logging.basicConfig(filename='webex_bot.log', level=logging.INFO)

# Function to run the entire process
def run_daily_summary():
    logging.info("Starting daily GitHub issue summary process.")
    
    # 1. Fetch new GitHub issues
    last_day = datetime.utcnow() - timedelta(days=1)
    new_issues = get_new_issues(last_day)

    # 2. Summarize the issues
    summary = summarize_issues(new_issues)

    # 3. Send the summary to Webex
    send_message_to_webex(summary)

# Schedule the job to run every day at 9:00 AM
schedule.every().day.at("09:00").do(run_daily_summary)

# Keep the script running with logging
if __name__ == "__main__":
    logging.info("Starting the Webex GitHub summary bot.")
    while True:
        schedule.run_pending()
        time.sleep(60)
