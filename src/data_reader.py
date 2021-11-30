import pandas as pd
import datetime


def read_post_data():
    """
    Read the post for the given day from the csv
    """
    start_day = datetime.date(2021, 12, 1)
    today = datetime.date.today()
    post_idx = (today - start_day).days + 1

    data = pd.read_csv("data/advent_data.csv")
    post = data[post_idx]

    return {
        "day_to_post": post.day_to_post,
        "resource_name": post.resource_name,
        "resource_description": post.resource_description,
        "resource_url": post.resource_url,
        "hashtags": post.hashtags,
    }
