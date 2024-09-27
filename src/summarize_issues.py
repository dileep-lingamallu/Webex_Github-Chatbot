import openai
import logging
import os

# OpenAI API Key (from environment variables)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

logging.basicConfig(filename='webex_bot.log', level=logging.INFO)

# Function to summarize GitHub issues using ChatGPT with better prompt
def summarize_issues(issues):
    if not issues:
        logging.info("No new issues to report.")
        return "No new issues to report."

    logging.info(f"Summarizing {len(issues)} issues.")
    
    # Prepare a concise prompt focusing on title and priorities
    issue_texts = [f"Issue #{issue['number']}: {issue['title']} (Priority: {issue.get('labels', 'No priority')})" for issue in issues]
    prompt = "Summarize the following GitHub issues by title and priority only:
" + "
".join(issue_texts)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can also use gpt-3.5-turbo for cost efficiency
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes GitHub issues for daily reporting."},
                {"role": "user", "content": prompt},
            ]
        )
        summary = response['choices'][0]['message']['content']
        logging.info("Successfully summarized issues.")
        return summary
    except Exception as e:
        logging.error(f"Error summarizing issues with OpenAI: {e}")
        return "Error summarizing the issues."
