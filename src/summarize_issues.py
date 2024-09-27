import openai

# OpenAI API Key
OPENAI_API_KEY = 'your_openai_api_key'

openai.api_key = OPENAI_API_KEY

# Function to summarize GitHub issues using ChatGPT
def summarize_issues(issues):
    if not issues:
        return "No new issues to report."

    # Prepare a prompt with issue details
    issue_texts = [f"Issue #{issue['number']}: {issue['title']}
Description: {issue['body']}
" for issue in issues]
    prompt = "Summarize the following GitHub issues in a concise report:
" + "
".join(issue_texts)
    
    # Call ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use gpt-3.5-turbo for cost efficiency
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes GitHub issues for daily reporting."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the summary from the response
    summary = response['choices'][0]['message']['content']
    return summary
