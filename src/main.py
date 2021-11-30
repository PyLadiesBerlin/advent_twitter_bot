import os
import sys

from loguru import logger

from config import Config
from data_reader import read_post_data
from notifications import send_email
from tweet import twitter_message, twitter_post, twitter_connect


logger = logger.bind(name="PyLadiesAdvent")


def main():

    config = Config()

    if not config.val_config():
        logger.info("Some environment variables do not exist.")
        sys.exit()

    env = config.CONF["ENV"]

    # Get post for the day
    advent_post = read_post_data(env)

    # Create twitter message
    message = twitter_message(
        env,
        advent_post["day_to_post"].values[0],
        advent_post["resource_name"].values[0],
        advent_post["resource_description"].values[0],
        advent_post["resource_url"].values[0],
        advent_post["hashtags"].values[0],
    )

    try:

        # Connect to Twitter
        api = twitter_connect(
            config.CONF["TWITTER_API_KEY"],
            config.CONF["TWITTER_API_SECRET_KEY"],
            config.CONF["TWITTER_ACCESS_TOKEN"],
            config.CONF["TWITTER_ACCESS_TOKEN_SECRET"],
        )

        logger.info("Connected to Twitter...")

        # Post to  Twitter
        # twitter_post(api, message)

        logger.info(f"The advent post has been posted! {message}")

    except Exception as e:
        logger.error(e)
        send_email(e, message, config.CONF["SENDGRID_API_KEY"], config.CONF["NOTIFY_EMAIL"])


if __name__ == "__main__":
    main()
