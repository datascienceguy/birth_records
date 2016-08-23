# from __future__ import print_function
from sklearn.svm import SVR
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import time
import gc

inputFilePath = '/Users/edye/data/birth_records/2014/2014_births_processed.txt'

def testSampleSize(X_all, y_all, num_test, num_train):
    print "Num train: {}, Num test: {}".format(num_train, num_test)

    X_train, X_test, y_train, y_test = \
        train_test_split(X_all, y_all, test_size=num_test, train_size=num_train, random_state=42)

    svmClf = SVR()

    start = time.time()
    svmClf.fit(X_train, y_train)
    end = time.time()
    print "Done!\nTraining time (secs): {:.3f}".format(end - start)

    start = time.time()
    y_pred = svmClf.predict(X_test)
    end = time.time()
    print "Done!\Predicting time (secs): {:.3f}".format(end - start)

    print 'MSE of train: {}'.format(mean_squared_error(y_train, svmClf.predict(X_train)))
    print 'MSE of test: {}'.format(mean_squared_error(y_test, y_pred))

births = pd.read_csv(inputFilePath,delimiter="\t")

# Extract feature (X) and target (y) columns
feature_cols = list(births.columns[2:])  # all columns but first two are features
target_col = births.columns[0]  # first column is the target/label

X_all = births[feature_cols]  # feature values for all students
y_all = births[target_col]  # corresponding targets/labels

# Free up some RAM
del births
gc.collect()


# Decide how many training vs test samples you want
sample_sizes = [10, 100, 1000, 10000, 100000]#, 500000, 750000, 1000000]
for sample_size in sample_sizes:
    num_train = int(sample_size*0.75)
    num_test = int(sample_size*0.25)
    testSampleSize(X_all, y_all, num_test, num_train)
