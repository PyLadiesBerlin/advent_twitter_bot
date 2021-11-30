from dotenv import load_dotenv
import os

# Load Environment variables
load_dotenv()


class Config:
    def __init__(self):

        self.CONF = {
            "TWITTER_USER": os.getenv("TWITTER_USER"),
            "TWITTER_API_KEY": os.getenv("TWITTER_API_KEY"),
            "TWITTER_API_SECRET_KEY": os.getenv("TWITTER_API_SECRET_KEY"),
            "TWITTER_BEARER_TOKEN": os.getenv("TWITTER_BEARER_TOKEN"),
            "TWITTER_ACCESS_TOKEN": os.getenv("TWITTER_ACCESS_TOKEN"),
            "SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY"),
            "NOTIFY_EMAIL": os.getenv("NOTIFY_EMAIL"),
        }

    def val_config(self):

        for c in self.CONF.keys():
            if self.CONF[c] == "":
                return False

        return True
