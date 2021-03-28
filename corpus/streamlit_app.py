import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

st.title('Corpus Explorer')

with open('corpus_files\\corpus_raw', 'rb') as f:
	data = pickle.load(f)

#data.drop(['title', 'body', 'score', 'comms_num'], axis=1, inplace=True)
st.text('This app explores a corpus of dream narratives scraped from Reddit.')

st.subheader('Raw data')
st_ms = st.multiselect("Columns", data.columns.tolist())
st.dataframe(data)


st.subheader('Post times by hour')
hist_values = np.histogram(
    data['timestamp'].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

df_temp = data.groupby(['text_length', 'comms_num']).mean()

st.dataframe(data)
