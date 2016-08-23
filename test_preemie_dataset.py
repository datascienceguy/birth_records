from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd
import time

inputFilePath = '/Users/edye/data/birth_records/2014/2014_births_processed.txt'
sample_size = 5000

births = pd.read_csv(inputFilePath,delimiter="\t")
feature_cols = list(births.columns[2:])  # all columns but first two are features
target_col = births.columns[0]  # first column is the target/label

# Extract feature (X) and target (y) columns
print "Feature column(s):-\n{}".format(feature_cols)
print "Target column: {}".format(target_col)
print "Total number of births: {}".format(len(births.index))

X_all = births[feature_cols]
y_all = births[target_col]

# Training set is 75% of the sample size, test set is 25%
num_train = int(sample_size*0.75)
num_test = int(sample_size*0.25)
X_train, X_test, y_train, y_test = \
    train_test_split(X_all, y_all, test_size=num_test, train_size=num_train, random_state=42)

# Initializing the Random Forest Regressor with optimal parameters
randClf = RandomForestRegressor(n_estimators=1000, min_samples_leaf=20)

start = time.time()
randClf.fit(X_train, y_train)
end = time.time()
print "Done!\nTraining time (secs): {:.3f}".format(end - start)

start = time.time()
y_pred = randClf.predict(X_test)
end = time.time()
print "Done!\Predicting time (secs): {:.3f}".format(end - start)

start = time.time()
y_pred = randClf.predict(X_test)
end = time.time()
print "Done!\Predicting time (secs): {:.3f}".format(end - start)

# Generate preemies dataset
preemies = births[births['01numWeeksAtBirthOE'] < 37].sample(n=1000)
preemies_features = preemies[feature_cols]
preemies_target = preemies[target_col]
preemies_pred = randClf.predict(preemies_features)

fullterms = births[births['01numWeeksAtBirthOE'] >= 37].sample(n=1000)
fullterms_features = fullterms[feature_cols]
fullterms_target = fullterms[target_col]
fullterms_pred = randClf.predict(fullterms_features)

print 'RMSE of train: {}'.format(sqrt(mean_squared_error(y_train, randClf.predict(X_train))))
print 'RMSE of test: {}'.format(sqrt(mean_squared_error(y_test, y_pred)))
print 'RMSE of preemies: {}'.format(sqrt(mean_squared_error(preemies_target, preemies_pred)))
print 'RMSE of full terms: {}'.format(sqrt(mean_squared_error(fullterms_target, fullterms_pred)))
