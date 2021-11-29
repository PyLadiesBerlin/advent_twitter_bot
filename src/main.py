import os
import sys

from loguru import logger
import tweepy

from config import Config
from notifications import send_email


logger = logger.bind(name="PyLadiesAdvent")


def main():

    env = Config()

    if not env.val_config():
        logger.info("Some environment variables do not exist.")
        sys.exit()

    try:
        # Get post for the day
        advent_post = read_post_data()

        # Connect to Wordpress and Twitter
        auth = tweepy.OAuthHandler("TWITTER_API_KEY", "TWITTER_API_SECRET_KEY")
        auth.set_access_token("TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET")
        api = api = tweepy.API(auth)

        logger.info("Connected to Twitter...")

        # Create twitter message
        message_twitter = twitter_message(
            advent_post.day_to_post,
            advent_post.resource_name,
            advent_post.resource_description,
            advent_post.resource_url,
            advent_post.hashtags,
        )

        # Post to  Twitter
        # twitter_post(api, message_twitter)

        logger.info("The advent post has been posted!")

    except Exception as e:
        send_email(e, env.CONF["SENDGRID_API_KEY"], env.CONF["NOTIFY_EMAIL"])


if __name__ == "__main__":
    main()