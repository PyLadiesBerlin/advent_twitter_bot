import datetime

from loguru import logger
import pandas as pd


logger = logger.bind(name="PyLadiesAdvent")


def read_post_data(env):
    """
    Read the post for the given day from the csv
    """
    # YYYY MM DD
    start_day = datetime.date(2021, 11, 30)
    today = datetime.date.today()
    post_idx = (today - start_day).days
    logger.debug(f"post index: {post_idx}")
    if post_idx < 0:
        raise Exception("It's not advent yet")

    if env == "dev":
        file_path = "src/data/advent_data.csv"
    else:
        file_path = "data/advent_data.csv"

    data = pd.read_csv(file_path)
    logger.debug(f"Retrieved data, length: {len(data)}")

    post = data.iloc[[post_idx]]
    logger.debug(f"Retrieved post: {post}")

    return {
        "day_to_post": post.day_to_post,
        "resource_name": post.resource_name,
        "resource_description": post.resource_description,
        "resource_url": post.resource_url,
        "hashtags": post.hashtags,
    }
