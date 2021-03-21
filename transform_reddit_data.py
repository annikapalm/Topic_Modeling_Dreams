from datetime import date
import pickle

def download_posts(subreddit):    
    """
    Transforms a subreddit object into a dictionary
    by iterating over every submission stored in that object and 
    saving the submission's data, such as their titles, bodies and IDs.
    The dictionary is saved as a pickle file
    
    Parameters:
    ----------
    subreddit : an object of the subreddit class

    
    credit: Rodrigues, Felippe (2018) "How to scrape Reddit with Python". 
    Retrived July 29, 2020, from https://www.storybench.org/how-to-scrape-reddit-with-python/
    """
    
    submission_dict = {'title': [],
                       'body' : [],
                       'url' : [],
                       'score' : [],
                       'comms_num' : [],
                       'id' : [],
                       'created' : []} 
              
    for submission in subreddit:
        submission_dict['title'].append(submission.title)
        submission_dict['body'].append(submission.selftext)
        submission_dict['id'].append(submission.id)
        submission_dict['url'].append(submission.url)
        submission_dict['score'].append(submission.score)
        submission_dict['comms_num'].append(submission.num_comments)
        submission_dict['created'].append(submission.created)

    current_date = str(date.today())

    with open('corpus\\corpus_files\\download-' + current_date + '.pkl', 'wb') as f:
      pickle.dump(submission_dict, f)
      print('Download successful')
