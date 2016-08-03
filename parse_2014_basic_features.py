from __future__ import print_function

inputDir = '/Users/edye/data/birth_records/2014'
inputFile = 'Nat2014PublicUS.c20150514.r20151022.txt'

outputFile = '2014_births.txt'
outPrint= file(outputFile, 'w')
printedHeader = False

def isfloat(value):
  try:
    return float(value)
  except:
    return None

def isInt(value):
  try:
    return int(value)
  except:
    return None


inputFilePath = inputDir + '/' + inputFile
with open(inputFilePath) as fp:
    for line in fp:
        row = {}
        # Make sure to subtract 1 from position in PDF guide
        # Second index of slice is excluded from string, so string[0:2], will give positions 0 and 1.

        # What attributes will be most useful for predicting future births?
        # All features selected should be available prior to delivery
        row['numWeeksAtBirthOE'] = {'99': None}.get(line[498:500], line[498:500])

        row['momAge'] = isInt({'99': None}.get(line[74:76], line[74:76]))
        row['momRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[106])
        row['isMomMarried'] = {'1': 1, '2': 0}.get(line[119], None)
        row['momBMI'] = isfloat({'99.9': None}.get(line[282:286], line[282:286]))
        row['momHeightInches'] = isInt({'99': None}.get(line[279:281], line[279:281]))
        row['momWeightGain'] = isInt({'99': None}.get(line[303:305], line[303:305]))
        row['momPrePregWeightPounds'] = isInt({'999': None}.get(line[291:294], line[291:294]))
        row['numYearsSincePeriod'] = isInt({'9999': None}.get(line[480:484], 2014-int(line[480:484])))
        row['isMomHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[123], 1)

        row['dadAge'] = isInt({'99': None}.get(line[146:148], line[146:148]))
        row['dadRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[151], None)
        row['isDadHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[161], 1)

        row['hadPriorTerminations'] = {'99': None, '00': 0}.get(line[172:174], 1)
        row['numMonthsSinceLastLiveBirth'] = isInt({'999':None, '888':None}.get(line[197:200], line[197:200]))
        row['hadPriorBirthAndDead'] = {'99': None, '00': 1}.get(line[172:174], 1)
        row['hadPriorBirthAndAlive'] = {'99': None, '00': 1}.get(line[170:172], 1)

        row['prenatalCareMonthBegan'] = isInt({'00':None, '99':None}.get(line[223:225], line[223:225]))
        row['numPrenatalVisits'] = isInt({'99':None}.get(line[237:239], line[237:239]))

        row['numDailyCigarettesPriorPreg'] = isInt({'99':None}.get(line[252:254], line[252:254]))
        row['numDailyCigarettesFirstTri'] = isInt({'99':None}.get(line[254:256], line[254:256]))
        row['numDailyCigarettesSecondTri'] = isInt({'99':None}.get(line[256:258], line[256:258]))
        row['numDailyCigarettesThirdTri'] = isInt({'99':None}.get(line[258:260], line[258:260]))

        row['prePregDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[312], None)
        row['gestationalDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[313], None)
        row['prePregHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[314], None)
        row['gestationalHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[315], None)
        row['hypertensionEclampsia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[316], None)
        row['noRiskFactors'] = {'1': 1, '0': 0, '9': None}.get(line[336], None)

        row['gonorrhea'] = {'Y': 1, 'N': 0, 'U': None}.get(line[342], None)
        row['syphylis'] = {'Y': 1, 'N': 0, 'U': None}.get(line[343], None)
        row['chlamydia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[344], None)
        row['hepatitisB'] = {'Y': 1, 'N': 0, 'U': None}.get(line[345], None)
        row['hepatitisC'] = {'Y': 1, 'N': 0, 'U': None}.get(line[346], None)
        row['noInfections'] = {'1': 1, '0': 0, '9': None}.get(line[352], None)

        row['prevPretermBirth'] = {'Y': 1, 'N': 0, 'U': None}.get(line[317], None)
        row['usedInfertility'] = {'Y': 1, 'N': 0, 'U': None}.get(line[324], None)
        row['fertilityEnhanceDrugs'] = {'Y': 1, 'N': 0, 'X': 0, 'U': None}.get(line[325], None)
        row['assistReproductiveTech'] = {'Y': 1, 'N': 0, 'X': 0, 'U': None}.get(line[326], None)

        if printedHeader == False:
            print(*row.keys(), sep="\t", file=outPrint)
            printedHeader = True

        print(*row.values(), sep="\t", file=outPrint)
