# from __future__ import print_function
import pandas as pd

inputFilePath = '/Users/edye/dev/birth_records/2014_births.txt'

d = pd.read_csv(inputFilePath,delimiter="\t", nrows=100000 )

# Extract feature (X) and target (y) columns
feature_cols = list(d.columns[2:])  # all columns but first two are features
target_col = d.columns[0]  # first column is the target/label
print "Feature column(s):-\n{}".format(feature_cols)
print "Target column: {}".format(target_col)
print "Total number of births: {}".format(len(d.index))
