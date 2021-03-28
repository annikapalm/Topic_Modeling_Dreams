import transform_reddit_data
import login

subreddit = login.login_data('login_data')

transform_reddit_data.download_posts(subreddit)