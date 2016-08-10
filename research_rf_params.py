from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

def performance_metric(label, prediction):
    return metrics.mean_squared_error(label, prediction)

# inputFilePath = '/Users/edye/data/birth_records/2014/2014_births_processed.txt'
inputFilePath = '/Users/edye/dev/birth_records/small_births_processed.txt'
births = pd.read_csv(inputFilePath,delimiter="\t")

# Extract feature (X) and target (y) columns
feature_cols = list(births.columns[2:])  # all columns but first two are features
target_col = births.columns[0]  # first column is the target/label

X_all = births[feature_cols]  # feature values for all students
y_all = births[target_col]  # corresponding targets/labels

# 500,000 was the best sample size while still giving the maximum accuracy
# Obtained by testing sample sizes
sample_size = 50000
num_train = int(sample_size*0.75)
num_test = int(sample_size*0.25)
X_train, X_test, y_train, y_test = \
    train_test_split(X_all, y_all, test_size=num_test, train_size=num_train, random_state=42)

parameters = {
    'n_estimators':(10,50,100,500,1000,5000),
    'max_features':(0.25,0.5,0.75)
}
randClf = RandomForestRegressor()
scorer = make_scorer(performance_metric, greater_is_better=False)
reg = GridSearchCV(randClf, parameters, scorer) # Maybe use cv=20?

# randClf.fit(X_train, y_train)
# y_pred = randClf.predict(X_test)
# print 'MSE of train: {}'.format(mean_squared_error(y_train, randClf.predict(X_train)))
# print 'MSE of test: {}'.format(mean_squared_error(y_test, y_pred))

# Fit the learner to the training data to obtain the best parameter set
print "Final Model: "
print reg.fit(X_train, y_train)
best_reg = reg.best_estimator_
print best_reg

y_pred = best_reg.predict(X_test)
print 'MSE of train: {}'.format(mean_squared_error(y_train, best_reg.predict(X_train)))
print 'MSE of test: {}'.format(mean_squared_error(y_test, y_pred))

importances = best_reg.feature_importances_
print importances
print feature_cols
# important_names = feature_cols[importances > np.mean(importances)]
# print important_names

# Use the model to predict the output of a particular sample
# x = [11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]
# y = best_reg.predict(x)
# print "House: " + str(x)
# print "Prediction: " + str(y)
