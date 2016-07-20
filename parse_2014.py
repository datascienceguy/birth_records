from __future__ import print_function

def printHeaderColumns(outPrint):
    print('dobYY', 'isBornInHospital',
          'momAge', 'isMomUSBorn', 'momRace', 'isMomMarried', 'isMomHSGrad', 'isMomCollegeGrad',
          'momHeightInches', 'momBMI', 'momPrePregWeightPounds', 'momDeliveryWeightPounds', 'momWeightGain',
          'dadAge', 'dadRace', 'isDadHSGrad', 'isDadCollegeGrad',
          'hadPriorBirthAndAlive', 'hadPriorBirthAndDead', 'hadPriorTerminations',
          'numMonthsSinceLastLiveBirth', 'numMonthsSinceLastPreg', 'numMonthsSinceLastOtherPreg',
          'prenatalCareMonthBegan', 'numPrenatalVisits', 'usedWIC',
          'numDailyCigarettesPriorPreg', 'numDailyCigarettesFirstTri', 'numDailyCigarettesSecondTri', 'numDailyCigarettesThirdTri',
          sep="\t", file=outPrint)

inputDir = '/Users/edye/data/birth_records/2014'
inputFile = 'Nat2014PublicUS.c20150514.r20151022.txt'
outputFile = '2014_births.txt'

outPrint= file(outputFile, 'w')
printHeaderColumns(outPrint)

inputFilePath = inputDir + '/' + inputFile
with open(inputFilePath) as fp:
    for line in fp:
        # Make sure to subtract 1 from position in PDF guide
        # Second index of slice is excluded from string, so string[0:2], will give positions 0 and 1.
        dobYY = line[8:12]
        dobMM = line[12:14]
        isBornInHospital = {'1': 1, '2': 0}.get(line[49], None) # This has lookup values

        momAge = {'99': None}.get(line[74:76], line[74:76])
        isMomUSBorn = {'1': 1, '2': 0}.get(line[83], None)
        momRace = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[106])
        isMomMarried = {'1': 1, '2': 0}.get(line[119], None)
        isMomHSGrad = {'1': 0, '2': 0, '9': None}.get(line[123], 1)
        isMomCollegeGrad = {'6': 1, '7': 1, '8': 1}.get(line[123], 0)
        momHeightInches = {'99': None}.get(line[279:281], line[279:281])
        momPrePregWeightPounds = {'999': None}.get(line[291:294], line[291:294])
        momDeliveryWeightPounds = {'999': None}.get(line[298:301], line[298:301])
        momWeightGain = {'99': None}.get(line[303:305], line[303:305])
        momBMI = {'99.9': None}.get(line[282:286], line[282:286])
        numYearsSincePeriod = {'9999', None}.get(line[480:484], dobYY-line[480:484])

        dadAge = {'99': None}.get(line[146:148], line[146:148])
        dadRace = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[151], None)
        isDadHSGrad = {'1': 0, '2': 0, '9': None}.get(line[161], 1)
        isDadCollegeGrad = {'6': 1, '7': 1, '8': 1}.get(line[161], 0)

        hadPriorBirthAndAlive = {'99': None, '00': 1}.get(line[170:172], 1)
        hadPriorBirthAndDead = {'99': None, '00': 1}.get(line[172:174], 1)
        hadPriorTerminations = {'99': None, '00': 0}.get(line[172:174], 1)
        numMonthsSinceLastLiveBirth = {'999':None, '888':None}.get(line[197:200], line[197:200])
        numMonthsSinceLastOtherPreg = {'999':None, '888':None}.get(line[205:208], line[205:208])
        numMonthsSinceLastPreg = {'999':None, '888':None}.get(line[213:216], line[213:216])

        prenatalCareMonthBegan = {'00':None, '99':None}.get(line[223:225], line[223:225])
        numPrenatalVisits = {'99':None}.get(line[237:239], line[237:239])
        usedWIC = {'Y': 1, 'N': 0, 'U': None}.get(line[250], None)

        numDailyCigarettesPriorPreg = {'99':None}.get(line[252:254], line[252:254])
        numDailyCigarettesFirstTri = {'99':None}.get(line[254:256], line[254:256])
        numDailyCigarettesSecondTri = {'99':None}.get(line[256:258], line[256:258])
        numDailyCigarettesThirdTri = {'99':None}.get(line[258:260], line[258:260])

        # Risk Factors
        prePregDiabetes = {'Y': 1, 'N': 0, 'U': None}.get(line[312], None)
        gestationalDiabetes = {'Y': 1, 'N': 0, 'U': None}.get(line[313], None)
        prePregHypertension = {'Y': 1, 'N': 0, 'U': None}.get(line[314], None)
        gestationalHypertension = {'Y': 1, 'N': 0, 'U': None}.get(line[315], None)
        hypertensionEclampsia = {'Y': 1, 'N': 0, 'U': None}.get(line[316], None)
        noRiskFactos = {'1': 1, '0': 0, '9': None}.get(line[336], None)

        # Infections
        gonorrhea = {'Y': 1, 'N': 0, 'U': None}.get(line[342], None)
        syphylis = {'Y': 1, 'N': 0, 'U': None}.get(line[343], None)
        chlamydia = {'Y': 1, 'N': 0, 'U': None}.get(line[344], None)
        hepatitisB = {'Y': 1, 'N': 0, 'U': None}.get(line[345], None)
        hepatitisC = {'Y': 1, 'N': 0, 'U': None}.get(line[346], None)
        noInfections = {'1': 1, '0': 0, '9': None}.get(line[352], None)

        prevPretermBirth = {'Y': 1, 'N': 0, 'U': None}.get(line[317], None)
        usedInfertility = {'Y': 1, 'N': 0, 'U': None}.get(line[325], None)
        fertilityEnhanceDrugs = {'Y': 1, 'N': 0, 'U': None}.get(line[326], None)
        assistReproductiveTech = {'Y': 1, 'N': 0, 'U': None}.get(line[327], None)

        # Obstetrics
        previousCSection = {'Y': 1, 'N': 0, 'U': None}.get(line[330], None)
        successfulBreech = {'Y': 1, 'N': 0, 'U': None}.get(line[359], None)
        failedBreech = {'Y': 1, 'N': 0, 'U': None}.get(line[360], None)

        # Labor and Delivery
        inductionOfLabor = {'Y': 1, 'N': 0, 'U': None}.get(line[382], None)
        augmentationOfLabor = {'Y': 1, 'N': 0, 'U': None}.get(line[383], None)
        steroids = {'Y': 1, 'N': 0, 'U': None}.get(line[384], None)
        antibiotics = {'Y': 1, 'N': 0, 'U': None}.get(line[385], None)
        chorioamnionitis = {'Y': 1, 'N': 0, 'U': None}.get(line[386], None)
        anesthesia = {'Y': 1, 'N': 0, 'U': None}.get(line[387], None)
        noCharacteristicsOfLabor = {'1': 1, '0': 0, '9': None}.get(line[394], None)

        # Method of Delivery
        isBreech = {'1': 0, '2': 1, '3': 0, '9': None}.get(line[401], None)
        isCephalic = {'1': 1, '2': 0, '3': 0, '9': None}.get(line[401], None)
        usedForceps = {'2': 1, '9': None}.get(line[401], 0)
        usedVacuum = {'3': 1, '9': None}.get(line[401], 0)
        wasCSectionDelivery = {'1': 0, '2': 1, '9': None}.get(line[407], None)
        wasVaginalDelivery = {'1': 1, '2': 0, '9': None}.get(line[407], None)

        # Maternal Morbidity
        maternalTransfusion = {'Y': 1, 'N': 0, 'U': None}.get(line[414], None)
        perinealLaceration = {'Y': 1, 'N': 0, 'U': None}.get(line[415], None)
        rupturedUterus = {'Y': 1, 'N': 0, 'U': None}.get(line[416], None)
        unplannedHysterectomy = {'Y': 1, 'N': 0, 'U': None}.get(line[417], None)
        admitToICU = {'Y': 1, 'N': 0, 'U': None}.get(line[418], None)
        noMorbidity = {'1': 1, '0': 0, '9': None}.get(line[426], None)

        # APGAR scores
        fiveMinuteAPGAR = {'99': None}.get(line[443:445], line[443:445])
        tenMinuteAPGAR = {'99': None, '88': None}.get(line[447:449], line[447:449])

        isTwin = {'2': 1}.get(line[453], 0)
        isTriplet = {'3': 1}.get(line[453], 0)
        isQuadruplet = {'4': 1}.get(line[453], 0)
        isQuintOrHigher = {'5': 1}.get(line[453], 0)

        isSecondInSet = {'2': 1, '9': None}.get(line[458], 0)
        isThirdInSet = {'3': 1, '9': None}.get(line[458], 0)
        isFourthOrHigherInSet = {'4': 1, '5': 1, '9': None}.get(line[458], 0)

        isMaleBaby = {'M':1}.get(line[474], 0)
        birthWeightInGrams = line[503:507]

        numWeeksAtBirthSinceLastPeriod = {'99': None}.get(line[489:491], line[489:491])
        numWeeksAtBirthObstetricEstimate = {'99': None}.get(line[491:493], line[491:493])

        # Abnormal conditons of newborn
        assistedVentilationImmediate = {'Y': 1, 'N': 0, 'U': None}.get(line[516], None)
        assistedVentilationAfter6Hrs = {'Y': 1, 'N': 0, 'U': None}.get(line[517], None)
        admittedToNICU = {'Y': 1, 'N': 0, 'U': None}.get(line[518], None)
        surfactant = {'Y': 1, 'N': 0, 'U': None}.get(line[519], None)
        antibioticsForNewborn = {'Y': 1, 'N': 0, 'U': None}.get(line[520], None)
        newbornSeizures = {'Y': 1, 'N': 0, 'U': None}.get(line[521], None)
        noAbnormalNewbornConditions = {'1': 1, '0': 0, '9': None}.get(line[530], None)

        # Congenital abnormalities
        anencephaly = {'Y': 1, 'N': 0, 'U': None}.get(line[536], None)
        spinaBifida = {'Y': 1, 'N': 0, 'U': None}.get(line[537], None)
        congenitalHeartDisease = {'Y': 1, 'N': 0, 'U': None}.get(line[538], None)
        congenitalHernia = {'Y': 1, 'N': 0, 'U': None}.get(line[539], None)
        omphalocele = {'Y': 1, 'N': 0, 'U': None}.get(line[540], None)
        gastroschisis = {'Y': 1, 'N': 0, 'U': None}.get(line[541], None)
        limbReduction = {'Y': 1, 'N': 0, 'U': None}.get(line[548], None)
        cleftLip = {'Y': 1, 'N': 0, 'U': None}.get(line[549], None)
        downSyndrome = {'C': 1, 'N': 0, 'P': None, 'U': None}.get(line[551], None)
        suspectedChromosomalDisorder = {'C': 1, 'N': 0, 'P': None, 'U': None}.get(line[552], None)
        hypospadias = {'Y': 1, 'N': 0, 'U': None}.get(line[553], None)
        noCongenitalAbnormalities = {'1': 1, '0': 0, '9': None}.get(line[560], None)


        print(dobYY, isBornInHospital,
              momAge, isMomUSBorn, momRace, isMomMarried, isMomHSGrad, isMomCollegeGrad,
              momHeightInches, momBMI, momPrePregWeightPounds, momDeliveryWeightPounds, momWeightGain,
              dadAge, dadRace, isDadHSGrad, isDadCollegeGrad,
              hadPriorBirthAndAlive, hadPriorBirthAndDead, hadPriorTerminations,
              numMonthsSinceLastLiveBirth, numMonthsSinceLastPreg, numMonthsSinceLastOtherPreg,
              prenatalCareMonthBegan, numPrenatalVisits, usedWIC,
              numDailyCigarettesPriorPreg, numDailyCigarettesFirstTri, numDailyCigarettesSecondTri, numDailyCigarettesThirdTri,

              sep="\t", file=outPrint)
