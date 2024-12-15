import os

# Fetching environment variables from GitHub Secrets
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Check if any required variable is missing
if not (REDDIT_USERNAME and REDDIT_PASSWORD and REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET and REDDIT_USER_AGENT):
    print("Missing required environment variables")
    exit(1)

# Bot configuration
TARGET_SUBREDDIT = "CucumberBotTestSub"  # Replace with your desired subreddit
TARGET_STRING = "test"  # Replace with your desired search string
REPLY_MESSAGE = "Hey, I like your comment!"  # Replace with your desired reply message

# Bot behavior configuration
SLEEP_DURATION = 10  # Adjust the sleep duration as needed in seconds
