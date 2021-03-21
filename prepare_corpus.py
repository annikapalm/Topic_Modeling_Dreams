import process_corpus_files
import pandas as pd

corpus_df = pd.DataFrame(columns=['title', 'body', 'url', 'score', 'comms_num', 'id', 'created'])

corpus_df = process_corpus_files.prepare_corpus(corpus_df)

corpus_df = process_corpus_files.fix_timestamp(corpus_df)

corpus_df = process_corpus_files.sort_timestamps(corpus_df)

corpus_df = process_corpus_files.join_texts(corpus_df)

process_corpus_files.save_corpus(corpus_df)