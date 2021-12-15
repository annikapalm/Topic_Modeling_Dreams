# import transform_reddit_data
# import login


# subreddit = login.login_data('login_data')

# transform_reddit_data.download_posts(subreddit)

import pandas as pd 
import praw
import os
from nltk import word_tokenize
from datetime import date
import pickle


def login_data(filename):

	try:
		with open(filename + '.txt') as f:
			data = f.readlines()

		data = [d.strip() for d in data]
		print(data)

		reddit = praw.Reddit(client_id=data[0],                         
                     		client_secret=data[1],                  
                     		user_agent=data[2],                        
                     		username=data[3],                          
                     		password=data[4])  

		subreddit = reddit.subreddit('Dreams')
		new_subreddit = subreddit.new(limit=1000)


	except EOFError as e:
		print(e)

	return new_subreddit

	import pickle
import datetime as dt


def download_posts(subreddit):    
    
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



def prepare_corpus(df):
    
    try:
        os.chdir(os.getcwd() + '\\corpus_files')
    except OSError as e:
        print(e)
    
    list_of_files = os.listdir()

    for file in list_of_files:
        if file[-4:] == '.pkl':
            print('Processing: ' + str(file))
            with open(file, 'rb') as f:
                dct = pickle.load(f)
        
                tmp_df = pd.DataFrame.from_dict(dct, orient='index').T
                #corpus_df = df.append(pd.DataFrame.from_dict(dct, orient='index').T)
                df = df.append(tmp_df, ignore_index=True)
        
    df.drop_duplicates(inplace=True)
    print('Done')
 
    return df


def get_date(created):
    
    return dt.datetime.fromtimestamp(created)


def fix_timestamp(df):
    
    _timestamp = df['created'].apply(get_date)
    df = df.assign(timestamp = _timestamp)
    df = df.drop('created', axis=1)
    
    return df

def sort_timestamps(df):

    df = df.sort_values('timestamp')

    return df


def join_texts(df):

    df['text'] = df['title'] + ' ' + df['body']
    
    return df


def save_corpus(df):

    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    
    try:
        filename = input('Filename: ')
        with open(filename + '.pkl', 'wb') as f:
            pickle.dump(df, f)
            print("Corpus file saved")
    except EOFError as e:
        print(e)


def load_raw_corpus():
	current = os.getcwd()
	if current[-6:] != 'corpus':
		try:
			os.chdir(os.getcwd() + '\\corpus')
		except OSError as e:
			print(e)
			return
	try:
		filename = input('Filename: ')
		with open(filename + '.pkl', 'rb') as f:
			df = pickle.load(f)
			print('Raw corpus data successfully loaded.')
	except OSError as e:
		print(e)
		return

	return df


def tokenize_texts(df, remove_short):
    
    df['tokenized_text'] = df['text'].apply(word_tokenize)
    
    if remove_short == True:
        df['text_length'] = df['tokenized_text'].str.len()
        try:
            min_word_count = input('Enter the desired minimum text length: ')
            df = df.loc[df['tokenized_text'].str.len() >= int(min_word_count)]
        except EOS as e:
            print(e)
            
    return df


subreddit = login_data('login_data')

download_posts(subreddit)

corpus_df = pd.DataFrame(columns=['title', 'body', 'url', 'score', 'comms_num', 'id', 'created'])

corpus_df = load_raw_corpus()

corpus_df = tokenize_texts(corpus_df, True)

corpus_df = prepare_corpus(corpus_df)

corpus_df = fix_timestamp(corpus_df)

corpus_df = sort_timestamps(corpus_df)

corpus_df = join_texts(corpus_df)

print(corpus_df)

#save_corpus(corpus_df)