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
        row['01numWeeksAtBirthOE'] = {'99': None}.get(line[498:500], line[498:500])
        row['02numWeeksAtBirthPeriod'] = {'99': None}.get(line[489:491], line[489:491])

        row['03momAge'] = isInt({'99': None}.get(line[74:76], line[74:76]))
        row['04momRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[106])
        row['05isMomMarried'] = {'1': 1, '2': 0}.get(line[119], None)
        row['06momBMI'] = isfloat({'99.9': None}.get(line[282:286], line[282:286]))
        row['07momHeightInches'] = isInt({'99': None}.get(line[279:281], line[279:281]))
        row['08momWeightGain'] = isInt({'99': None}.get(line[303:305], line[303:305]))
        row['09momPrePregWeightPounds'] = isInt({'999': None}.get(line[291:294], line[291:294]))
        row['10numYearsSincePeriod'] = isInt({'9999': None}.get(line[480:484], 2014-int(line[480:484])))
        row['11isMomHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[123], 1)

        row['12dadAge'] = isInt({'99': None}.get(line[146:148], line[146:148]))
        row['13dadRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[151], None)
        row['14isDadHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[161], 1)

        row['15hadPriorTerminations'] = {'99': None, '00': 0}.get(line[172:174], 1)
        row['16numMonthsSinceLastLiveBirth'] = isInt({'999':None, '888':None}.get(line[197:200], line[197:200]))
        row['17hadPriorBirthAndDead'] = {'99': None, '00': 1}.get(line[172:174], 1)
        row['18hadPriorBirthAndAlive'] = {'99': None, '00': 1}.get(line[170:172], 1)

        row['19prenatalCareMonthBegan'] = isInt({'00':None, '99':None}.get(line[223:225], line[223:225]))
        row['20numPrenatalVisits'] = isInt({'99':None}.get(line[237:239], line[237:239]))

        row['21numDailyCigarettesPriorPreg'] = isInt({'99':None}.get(line[252:254], line[252:254]))
        row['22numDailyCigarettesFirstTri'] = isInt({'99':None}.get(line[254:256], line[254:256]))
        row['23numDailyCigarettesSecondTri'] = isInt({'99':None}.get(line[256:258], line[256:258]))
        row['24numDailyCigarettesThirdTri'] = isInt({'99':None}.get(line[258:260], line[258:260]))

        row['25prePregDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[312], None)
        row['26gestationalDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[313], None)
        row['27prePregHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[314], None)
        row['28gestationalHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[315], None)
        row['29hypertensionEclampsia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[316], None)
        row['30noRiskFactors'] = {'1': 1, '0': 0, '9': None}.get(line[336], None)

        row['31gonorrhea'] = {'Y': 1, 'N': 0, 'U': None}.get(line[342], None)
        row['32syphylis'] = {'Y': 1, 'N': 0, 'U': None}.get(line[343], None)
        row['33chlamydia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[344], None)
        row['34hepatitisB'] = {'Y': 1, 'N': 0, 'U': None}.get(line[345], None)
        row['35hepatitisC'] = {'Y': 1, 'N': 0, 'U': None}.get(line[346], None)
        row['36noInfections'] = {'1': 1, '0': 0, '9': None}.get(line[352], None)

        row['37prevPretermBirth'] = {'Y': 1, 'N': 0, 'U': None}.get(line[317], None)
        row['38usedInfertility'] = {'Y': 1, 'N': 0, 'U': None}.get(line[324], None)
        row['39fertilityEnhanceDrugs'] = {'Y': 1, 'N': 0, 'X': 0, 'U': None}.get(line[325], None)
        row['40assistReproductiveTech'] = {'Y': 1, 'N': 0, 'X': 0, 'U': None}.get(line[326], None)

        if printedHeader == False:
            print(*sorted(row.keys()), sep="\t", file=outPrint)
            printedHeader = True
        else:
            print(*([r[1] for r in sorted(row.items())]), sep="\t", file=outPrint)
