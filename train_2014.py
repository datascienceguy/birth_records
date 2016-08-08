# from __future__ import print_function
import pandas as pd

inputFilePath = '/Users/edye/dev/birth_records/small_births.txt'

births = pd.read_csv(inputFilePath,delimiter="\t", nrows=100 )

# Extract feature (X) and target (y) columns
feature_cols = list(births.columns[1:])  # all columns but first two are features
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

# First, decide how many training vs test samples you want
num_all = births.shape[0]  # same as len(student_data)
num_train = int(num_all * 0.75)  # about 75% of the data
num_test = num_all - num_train

# TODO: Then, select features (X) and corresponding labels (y) for the training and test sets
# Note: Shuffle the data or randomly select samples to avoid any bias due to ordering in the dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X_all, y_all, test_size=num_test, train_size=num_train, random_state=42)

print "Training set: {} samples".format(X_train.shape[0])
print "Test set: {} samples".format(X_test.shape[0])
# Note: If you need a validation set, extract it from within training data

# Train a model
import time

def train_classifier(clf, X_train, y_train):
    print "Training {}...".format(clf.__class__.__name__)
    start = time.time()
    clf.fit(X_train, y_train)
    end = time.time()
    print "Done!\nTraining time (secs): {:.3f}".format(end - start)

# Predict on training set and compute F1 score
from sklearn.metrics import f1_score

def predict_labels(clf, features, target):
    print "Predicting labels using {}...".format(clf.__class__.__name__)
    start = time.time()
    y_pred = clf.predict(features)
    end = time.time()
    print "Done!\nPrediction time (secs): {:.3f}".format(end - start)
    print target.values
    print y_pred
    # return f1_score(target.values, y_pred, average="macro")
    return clf.score(target.values, y_pred)

# Train and predict using different training set sizes
def train_predict(clf, X_train, y_train, X_test, y_test):
    print "------------------------------------------"
    print "Training set size: {}".format(len(X_train))
    train_classifier(clf, X_train, y_train)
    print "F1 score for training set: {}".format(predict_labels(clf, X_train, y_train))
    print "F1 score for test set: {}".format(predict_labels(clf, X_test, y_test))

# # TODO: Run the helper function above for desired subsets of training data
# # Note: Keep the test set constant
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import SGDClassifier
#from sklearn.neighbors.nearest_centroid import NearestCentroid

from sklearn.ensemble import RandomForestRegressor


classifiers = []
classifiers.append(RandomForestRegressor())
# classifiers.append(GradientBoostingClassifier())
# classifiers.append(SVC())
# classifiers.append(KNeighborsClassifier())
# classifiers.append(SGDClassifier(shuffle=True))
#classifiers.append(NearestCentroid())


for classifier in classifiers:
    for train_size in [int(num_train*0.25), int(num_train*0.5), int(num_train*0.75), num_train]:
        train_predict(classifier, X_train[:train_size], y_train[:train_size], X_test, y_test)

# TODO: Fine-tune your model and report the best F1 score
# from sklearn.grid_search import GridSearchCV
# from sklearn.metrics import f1_score, make_scorer
#
# svmClassifier = SVC()
#
# parameters = {'C':[0.1, 0.5, 1, 5, 10, 30, 50, 100, 1000], \
#               'gamma':[0.001, 0.01, 0.1, 0.5, 1, 2] \
#              }
# scorer = make_scorer(f1_score, pos_label="yes", average="macro")
# gsClassifier = GridSearchCV(estimator=svmClassifier, param_grid=parameters, scoring=scorer, cv=5)
# print "Final Model: "
# gsClassifier.fit(X_train, y_train)
# best_classifier = gsClassifier.best_estimator_
# print best_classifier
# train_predict(best_classifier, X_train, y_train, X_test, y_test)
