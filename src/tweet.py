import tweepy
from jinja2 import Environment, FileSystemLoader


def twitter_connect(
    TWITTER_API_KEY,
    TWITTER_API_SECRET_KEY,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
):
    """
    Connects to Twitter and return twitter object
    """
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


def twitter_message(post_day, name, description, url, hashtags):
    """
    Creates twitter message
    Inputs:
        post_day: int, day since the project started
        name: str
        description: str
        url: str, url for project
        hashtags: str, resource specific tags
    returns:
        280 characters string
    """

    # Message must be 2 characters shorter (278)
    lim = 280 - 2

    file_loader = FileSystemLoader("src/templates")
    env = Environment(loader=file_loader)
    if post_day == 0:
        template = env.get_template("day_0_template.txt")
    else:
        template = env.get_template("tweet_template.txt")

    text = template.render(
        post_day=str(post_day),
        name=name,
        description=description,
        url=url,
        hashtags=hashtags,
    )

    if len(text) > lim:
        content_text = text[:lim]
    else:
        content_text = text

    return content_text


def twitter_post(api, message_twitter):
    """
    Posts to twitter
    """
    api.update_status(status=message_twitter)
