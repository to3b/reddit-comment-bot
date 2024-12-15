import os
import praw
import time
import logging
from config import (
    REDDIT_USERNAME,
    REDDIT_PASSWORD,
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    TARGET_SUBREDDIT,
    TARGET_STRING,
    REPLY_MESSAGE,
    SLEEP_DURATION,
)

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to log in to Reddit
def bot_login():
    logger.info("Logging in...")
    
    try:
        reddit_instance = praw.Reddit(
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD,
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        logger.info("Logged in!")
        return reddit_instance
    except Exception as e:
        logger.error(f"Login failed: {e}")
        raise

# Function to process comments
def process_comments(reddit_instance, comments_replied_to):
    logger.info(f"Searching for new comments in subreddit {TARGET_SUBREDDIT}...")

    try:
        for comment in reddit_instance.subreddit(TARGET_SUBREDDIT).stream.comments():
            process_single_comment(comment, comments_replied_to)
    except Exception as e:
        logger.error(f"Error while fetching comments: {e}")

# Function to process a single comment
def process_single_comment(comment, comments_replied_to):
    try:
        if (
            TARGET_STRING.lower() in comment.body.lower()  # Case-insensitive search
            and comment.id not in comments_replied_to
            and comment.author != reddit_instance.user.me()  # Prevent the bot from replying to its own comment
        ):
            logger.info(f"String '{TARGET_STRING}' found in comment {comment.id}, replying...")
            comment.reply(REPLY_MESSAGE)  # Reply with the predefined message

            # Log the comment ID that has been replied to
            comments_replied_to.append(comment.id)
            logger.info(f"Replied to comment {comment.id}")

            # Save the comment ID to a file so it doesn't reply to it again in the future
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
    except Exception as e:
        logger.error(f"Error replying to comment {comment.id}: {e}")

# Function to get saved comments
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = [comment.strip() for comment in f.readlines() if comment.strip()]
    return comments_replied_to

# Main function to run the bot
if __name__ == "__main__":
    reddit_instance = bot_login()
    comments_replied_to = get_saved_comments()

    logger.info(f"Number of comments replied to: {len(comments_replied_to)}")

    while True:
        try:
            process_comments(reddit_instance, comments_replied_to)
        except KeyboardInterrupt:
            logger.info("Bot terminated by user.")
            break
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            time.sleep(int(SLEEP_DURATION))  # Retry after a short delay
