import preprocessing_tasks
import process_corpus_files
import pickle
import os
import pandas as pd


corpus_df = preprocessing_tasks.load_raw_corpus()

corpus_df = preprocessing_tasks.tokenize_texts(corpus_df, True)

### TEMPORARY

texts = corpus_df['text'].to_list()
with open('text.pkl', 'wb') as f:
	pickle.dump(texts, f)

process_corpus_files.save_corpus(corpus_df)