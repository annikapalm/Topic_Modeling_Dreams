import os
import pandas as pd
import pickle
import datetime as dt


def prepare_corpus(df):
    
    try:
        os.chdir(os.getcwd() + '\\corpus\\corpus_files')
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
    except EOFError as e:
        print(e)

    
               
    