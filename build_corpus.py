import praw
import pickle
import os
import pandas as pd
from datetime import date
import reddit_login
import transform_reddit_data


# Instantiate PRAW's Reddit() object with the required arguments.


reddit = reddit_login.login('login_data')


# Access and save the \dreams subreddit as a subreddit object.

subreddit = reddit.subreddit('Dreams')


# The subreddit object's posts of the category 'new' are downloaded. The maximum download limit is 1000 submissions.

new_subreddit = subreddit.new(limit=1000)


transform_reddit_data.download_posts(new_subreddit)
