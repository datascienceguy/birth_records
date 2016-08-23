from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from math import sqrt
import pandas as pd
import time

inputFilePath = '/Users/edye/dev/birth_records/small_births_processed.txt'

births = pd.read_csv(inputFilePath,delimiter="\t")
preemies = births[ births['01numWeeksAtBirthOE'] < 37]
fullTerm = births[ births['01numWeeksAtBirthOE'] >= 37]

print 'Train_time\tPredict_time\tSample_Size\tPreemie_pct\tfull_term_sample_size\tRMSE_train\tRMSE_test\tRMSE_preemie\tRMSE_full_term'

for sample_size in [100, 500, 1000, 5000, 10000, 50000, 100000, 250000, 500000]:
    for preemie_pct in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        try:
            num_preemies = int(sample_size*preemie_pct)
            num_fullterms = int(sample_size*(1-preemie_pct))

            # Over-sample births data using 50% preemie data (< 37 weeks) and 50% full-term births (>= 37 weeks)
            resampledBirths = preemies.sample(n=num_preemies)
            resampledBirths = resampledBirths.append( fullTerm.sample(n=num_fullterms) )

            # Extract feature (X) and target (y) columns
            feature_cols = list(resampledBirths.columns[2:])  # all columns but first two are features
            target_col = resampledBirths.columns[0]  # first column is the target/label

            X_all = resampledBirths[feature_cols]  # feature values for all students
            y_all = resampledBirths[target_col]  # corresponding targets/labels

            num_train = int(sample_size*0.75)-1
            num_test = int(sample_size*0.25)-1
            X_train, X_test, y_train, y_test = \
                train_test_split(X_all, y_all, test_size=num_test, train_size=num_train, random_state=42)

            randClf = RandomForestRegressor(n_estimators=1000, min_samples_leaf=20)

            start = time.time()
            randClf.fit(X_train, y_train)
            end = time.time()
            train_time = end - start
            # print "Done!\nTraining time (secs): {:.3f}".format(end - start)

            start = time.time()
            y_pred = randClf.predict(X_test)
            end = time.time()
            predict_time = end - start
            # print "Done!\Predicting time (secs): {:.3f}".format(end - start)

            # Generate preemies dataset
            preemiesToTest = preemies.sample(n=1000)
            preemiesToTest_features = preemiesToTest[feature_cols]
            preemiesToTest_target = preemiesToTest[target_col]
            preemiesToTest_pred = randClf.predict(preemiesToTest_features)

            # Generate full term dataset
            fulltermsToTest = fullTerm.sample(n=1000)
            fulltermsToTest_features = fulltermsToTest[feature_cols]
            fulltermsToTest_target = fulltermsToTest[target_col]
            fulltermsToTest_pred = randClf.predict(fulltermsToTest_features)

            rmse_train = sqrt(mean_squared_error(y_train, randClf.predict(X_train)))
            rmse_test = sqrt(mean_squared_error(y_test, y_pred))
            rmse_preemie = sqrt(mean_squared_error(preemiesToTest_target, preemiesToTest_pred))
            rmse_full_term = sqrt(mean_squared_error(fulltermsToTest_target, fulltermsToTest_pred))
            print '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(train_time, predict_time, sample_size, preemie_pct, num_fullterms, rmse_train, rmse_test, rmse_preemie, rmse_full_term)

            # print 'Sample size: {}\t'.format(sample_size)
            # print 'Preemie percentage: {}'.format(preemie_pct)
            # print 'Full Term sample size: {}'.format(num_fullterms)
            #
            # print 'RMSE of train: {}'.format(sqrt(mean_squared_error(y_train, randClf.predict(X_train))))
            # print 'RMSE of test: {}'.format(sqrt(mean_squared_error(y_test, y_pred)))
            # print 'RMSE of preemies: {}'.format(sqrt(mean_squared_error(preemiesToTest_target, preemiesToTest_pred)))
            # print 'RMSE of full terms: {}'.format(sqrt(mean_squared_error(fulltermsToTest_target, fulltermsToTest_pred)))
            # print '\n\n'
        except:
            print 'Error at sample_size: {}, and preemie_pct: {}'.format(sample_size, preemie_pct)
