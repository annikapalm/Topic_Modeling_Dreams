import praw
import os


def login_data(filename):
	"""
	Reads in the contents of a textfile that holds the login data
    required for API authentication with the praw module
    The data is then used to authenticate the API user

    Parameter : 
    ---------
    filename of the .txt file holding the login data

    Returns :
    -------
    a new object of the Reddit class
    """

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