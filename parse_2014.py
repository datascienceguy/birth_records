inputDir = '/Users/dmaier/DataScience/udacity/machine_learning/nanodegree/capstone_project/data/2014_births'
inputFile = 'Nat2014PublicUS.c20150514.r20151022.txt'

inputFilePath = inputDir + '/' + inputFile
with open(inputFilePath) as fp:
    for line in fp:
        dobYY = line[9:12]
        dobMM = line[13:14]
        isBornInHospital = {1: 1, 2: 0}.get(line[50], None) # This has lookup values

        momAge = line[75:76]
        isMomUSBorn = {1: 1, 2: 0}.get(line[84], None)
        momRace = {1: 'White', 2: 'Black', 3: 'AIAN', 4: 'Asian', 5: 'NHOPI', 6: 'Multi'}.get(line[107])
        isMomMarried = {1: 1, 2: 0}.get(line[120], None)
        isMomHSGrad = {1: 0, 2: 0, 9: None}.get(line[124], 1)
        isMomCollegeGrad = {6: 1, 7: 1, 8: 1}.get(line[124], 0)

        dadAge = line[147:148]
        dadRace = {1: 'White', 2: 'Black', 3: 'AIAN', 4: 'Asian', 5: 'NHOPI', 6: 'Multi'}.get(line[153], None)
        isDadHSGrad = {1: 0, 2: 0, 9: None}.get(line[163], 1)
        isDadCollegeGrad = {6: 1, 7: 1, 8: 1}.get(line[163], 0)

        hadPriorBirthAndAlive = True if line[171:172] > '00' else False
        hadPriorBirthAndDead = True if line[171:172] > '00' else False
        numPriorBirthDead = line[171:172]
        prenatalCareMonthBegan = line[224:227]
        babyGender = line[475]
        numBornAtDelivery = line[454]
        birthWeight = line[504:507]
