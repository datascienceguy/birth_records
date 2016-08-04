# from __future__ import print_function
import pandas as pd

inputFilePath = '/Users/edye/dev/birth_records/2014_births.txt'

births = pd.read_csv(inputFilePath,delimiter="\t", nrows=100000 )

# Extract feature (X) and target (y) columns
feature_cols = list(births.columns[2:])  # all columns but first two are features
target_col = births.columns[0]  # first column is the target/label
print "Feature column(s):-\n{}".format(feature_cols)
print "Target column: {}".format(target_col)
print "Total number of births: {}".format(len(births.index))

X_all = births[feature_cols]  # feature values for all students
y_all = births[target_col]  # corresponding targets/labels
print "\nFeature values:-"
print X_all.head()  # print the first 5 rows
print "\Target values:-"
print y_all.head()  # print the first 5 rows
