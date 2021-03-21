from nltk import word_tokenize
import pandas as pd
import os
import pickle


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