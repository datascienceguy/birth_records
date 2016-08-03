from __future__ import print_function
import pandas as pd

inputFilePath = '/Users/edye/dev/birth_records/2014_births.txt'

d = pd.read_csv(inputFilePath,delimiter="\t", nrows=1000 )
print(d.numWeeksAtBirthSinceLastPeriod) 
