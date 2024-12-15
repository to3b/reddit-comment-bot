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
TARGET_SUBREDDIT = "AnarchyChess"  # Replace with your desired subreddit
TARGET_STRING = "google en passant"  # Replace with your desired search string
REPLY_MESSAGE = """
Okay, I just can’t do this anymore. Do you want me to say “holy hell” like every other free thinking NPC on this godforsaken website?

Think again, liberal sheep.

I am a true free thinker, like Ben Shapiro and Joe Rogan have taught me to me. I won’t succumb to your so called “joke”.

Call the exorcist! Bishop goes on vacation, fuck off, i was there when they first commented “Google En Passant” but now look at what you’ve turned this meme into. Just like ever other meme posted in r/anarchychess, it’s not funny, never was, never will be. What will he funny is when you all realise you’re just another sheep in the herd.

You want a new response to drop? Then here it is, libtard
"""  # Replace with your desired reply message

# Bot behavior configuration
SLEEP_DURATION = 10  # Adjust the sleep duration as needed in seconds
