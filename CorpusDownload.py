# Class for downloading user posts from Reddit and pickling them as dictionary for further processing

import praw
import pickle
from datetime import date

class CorpusDownloader:

    def __init__(self, path):

        self.path = path
        self.dct = None

    def download_posts(subreddit):
        """
        Transforms a subreddit object into a dictionary
        by iterating over every submission stored in that object and
        saving the submission's data, such as their titles, bodies and IDs.
        The dictionary is saved as a pickle file

        Parameters:
        ----------
        subreddit : an object of the subreddit class
        """

        dct = {'title': [],
                           'body': [],
                           'url': [],
                           'score': [],
                           'comms_num': [],
                           'id': [],
                           'created': []}

        for submission in subreddit:
            dct['title'].append(submission.title)
            dct['body'].append(submission.selftext)
            dct['id'].append(submission.id)
            dct['url'].append(submission.url)
            dct['score'].append(submission.score)
            dct['comms_num'].append(submission.num_comments)
            dct['created'].append(submission.created)

        current_date = str(date.today())

        with open('corpus\\download-' + current_date + '.pkl', 'wb') as f:
            pickle.dump(submission_dict, f)
            print('Download successful')
