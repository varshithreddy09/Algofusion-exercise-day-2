# word_count.py

import pandas as pd
import string
from collections import Counter

def remove_punc(str1):
    translator = str.maketrans('', '', string.punctuation)
    return str1.translate(translator)

def word_split(str2):
    return str2.split()

def word_dict(L1):
    return dict(Counter(L1))

def word_freq_table(d1):
    df = pd.DataFrame(list(d1.items()), columns=['word', 'No of occurrences'])
    return df
