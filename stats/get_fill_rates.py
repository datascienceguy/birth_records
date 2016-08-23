# from __future__ import print_function
import pandas as pd
import numpy as np
import math

inputFilePath = '/Users/edye/data/birth_records/2014/2014_births.txt'

def getFillRate(x):
    # Get counts of each value
    numNulls = x[np.isnan(x)]
    print numNulls
    # print x.count()
    # unique, counts = np.unique(x, return_counts=True)
    # ary = np.asarray((unique, counts)).T
    # print ary

births = pd.read_csv(inputFilePath,delimiter="\t")
blah = births.isnull().sum()
blah /= births.count() * 1.
print blah

# For each column in data, get frequencies of values and set for null values
# for column in births:
    # getFillRate(births[column])
    # freqs = getFrequencies(births[column])
