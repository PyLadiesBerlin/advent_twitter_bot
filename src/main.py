import os
import sys

from loguru import logger

from config import Config
from data_reader import read_post_data
from notifications import send_email
from tweet import twitter_message, twitter_post, twitter_connect


logger = logger.bind(name="PyLadiesAdvent")


def main():

    env = Config()

    if not env.val_config():
        logger.info("Some environment variables do not exist.")
        sys.exit()

    try:
        # Get post for the day
        advent_post = read_post_data()

        # Connect to Twitter
        api = twitter_connect(
            env.CONF["TWITTER_API_KEY"],
            env.CONF["TWITTER_API_SECRET_KEY"],
            env.CONF["TWITTER_ACCESS_TOKEN"],
            env.CONF["TWITTER_ACCESS_TOKEN_SECRET"],
        )

        logger.info("Connected to Twitter...")

        # Create twitter message
        message = twitter_message(
            advent_post["day_to_post"].values[0],
            advent_post["resource_name"].values[0],
            advent_post["resource_description"].values[0],
            advent_post["resource_url"].values[0],
            advent_post["hashtags"].values[0],
        )

        # Post to  Twitter
        twitter_post(api, message)

        logger.info("The advent post has been posted!")

    except Exception as e:
        logger.error(e)
        send_email(e, env.CONF["SENDGRID_API_KEY"], env.CONF["NOTIFY_EMAIL"])


if __name__ == "__main__":
    main()
