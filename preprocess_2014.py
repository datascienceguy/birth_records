# from __future__ import print_function
import pandas as pd
import numpy as np
import math

inputFilePath = '/Users/edye/dev/birth_records/2014_births.txt'
outputFilePath = '/Users/edye/dev/birth_records/2014_births_processed.txt'


def getFrequencies(x):
    # Remove all non-null values
    nonNulls = x[~np.isnan(x)]

    # Get counts of each value
    unique, counts = np.unique(nonNulls, return_counts=True)

    # Divide counts by total to get frequencies
    return np.asarray((unique, counts/(nonNulls.count()*1.))).T

def getRandValueByDistr(frequencies):
    return np.random.choice(frequencies[:,0], p=frequencies[:,1])

births = pd.read_csv(inputFilePath,delimiter="\t")
newBirths = births.copy(deep=False)

# For each column in data, get frequencies of values and set for null values
for column in births:
    freqs = getFrequencies(births[column])
    newBirths[column] = births[column].apply(lambda x: getRandValueByDistr(freqs) if math.isnan(x) else x)
    # births[column].apply()

newBirths.to_csv(outputFilePath, sep='\t', index=False)


# Some things we can do to preprocess the data:
# 1) To fill in null values, we can randomly select a value from the
#    entire set of values for that feature
