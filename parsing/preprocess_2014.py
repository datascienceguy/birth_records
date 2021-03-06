# from __future__ import print_function
import pandas as pd
import numpy as np
import math

inputFilePath = '/Users/edye/data/birth_records/2014/2014_births.txt'
outputFilePath = '/Users/edye/data/birth_records/2014/2014_births_processed.txt'

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

    # For all null values, select a value at random from the distribution within the column
    # By using the same frequency of the non-null data within the column,
    # we do not add noise to the data set.
    newBirths[column] = births[column].apply(lambda x: getRandValueByDistr(freqs) if math.isnan(x) else x)

# Using float_format='%.f' to save space in data file.  No need o store floating points
# for all the int columns.  This was tripling size of post_processed file.a
newBirths.to_csv(outputFilePath, sep='\t', index=False, float_format='%.f')
