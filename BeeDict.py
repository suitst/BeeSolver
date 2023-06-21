# create a dictionary of suitable words for spelling bee

import pandas as pd

raw = pd.read_csv('./words.csv', encoding='utf-8', engine='c')

proc = raw.drop(raw[raw['Words'].str.len() < 4].index)

proc.to_csv('./words_proc.csv', index=False)
