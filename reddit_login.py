import praw 
import csv

def login(filename):

    """"
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
        login_data = []
        with open(filename + '.txt') as file:
            print('Login data: ' + '\n')
            for line in file.readlines():
                login_data.append(line.strip())
            print(login_data)
    except IOError:
        print("Error: File does not exist.")
        return
            
    reddit = praw.Reddit(client_id=login_data[0],         # The app's client ID
                         client_secret=login_data[1],     # Client's verification code
                         user_agent=login_data[2],        # The app's name
                         username=login_data[3],          # The account user name
                         password=login_data[4])          # The account's password
        
    return reddit