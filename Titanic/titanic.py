#Titanic

from pandas import Series, DataFrame
from collections import Counter

import pandas as pd
import numpy as np
import collections

# Read csv into pandas.core.frame.DataFrame object
titanicTrain = pd.read_csv('/Users/simonzhang/scripts/data/train.csv', sep=',')
titanicTest = pd.read_csv('/Users/simonzhang/scripts/data/test.csv', sep=',')

# Take sample of file to work with
tit = titanicTrain[:25]

# define counter object to get descriptive overview of titles
cnt = Counter()

def acquire_substring(string):
    full_name = string.split(', ')
    last, first = full_name[0], full_name[1]
    pattern = r'[^\.]*'
    prog = re.compile(pattern)
    result = prog.match(first)
    cnt[result.group(0)] += 1
    return result.group(0)

def acquire_cabin_prefix(string):
	pattern = r'[A-Z]'



tit['Title'] = tit['Name'].map(lambda row: acquire_substring(row))
