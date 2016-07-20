from __future__ import print_function

inputDir = '/Users/edye/data/birth_records/2014'
inputFile = 'Nat2014PublicUS.c20150514.r20151022.txt'

outputFile = '2014_births.txt'
outPrint= file(outputFile, 'w')
printedHeader = False

inputFilePath = inputDir + '/' + inputFile
with open(inputFilePath) as fp:
    for line in fp:
        row = {}
        # Make sure to subtract 1 from position in PDF guide
        # Second index of slice is excluded from string, so string[0:2], will give positions 0 and 1.
        row['dobYY'] = line[8:12]
        row['dobMM'] = line[12:14]
        row['isBornInHospital'] = {'1': 1, '2': 0}.get(line[49], None) # This has lookup values

        # Mom stats
        row['momAge'] = {'99': None}.get(line[74:76], line[74:76])
        row['isMomUSBorn'] = {'1': 1, '2': 0}.get(line[83], None)
        row['momRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[106])
        row['isMomMarried'] = {'1': 1, '2': 0}.get(line[119], None)
        row['isMomHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[123], 1)
        row['isMomCollegeGrad'] = {'6': 1, '7': 1, '8': 1}.get(line[123], 0)
        row['momHeightInches'] = {'99': None}.get(line[279:281], line[279:281])
        row['momPrePregWeightPounds'] = {'999': None}.get(line[291:294], line[291:294])
        row['momDeliveryWeightPounds'] = {'999': None}.get(line[298:301], line[298:301])
        row['momWeightGain'] = {'99': None}.get(line[303:305], line[303:305])
        row['momBMI'] = {'99.9': None}.get(line[282:286], line[282:286])
        row['numYearsSincePeriod'] = {'9999': None}.get(line[480:484], int(row['dobYY'])-int(line[480:484]))

        # Dad stats
        row['dadAge'] = {'99': None}.get(line[146:148], line[146:148])
        row['dadRace'] = {'1': 'White', '2': 'Black', '3': 'AIAN', '4': 'Asian', '5': 'NHOPI', '6': 'Multi'}.get(line[151], None)
        row['isDadHSGrad'] = {'1': 0, '2': 0, '9': None}.get(line[161], 1)
        row['isDadCollegeGrad'] = {'6': 1, '7': 1, '8': 1}.get(line[161], 0)

        row['hadPriorBirthAndAlive'] = {'99': None, '00': 1}.get(line[170:172], 1)
        row['hadPriorBirthAndDead'] = {'99': None, '00': 1}.get(line[172:174], 1)
        row['hadPriorTerminations'] = {'99': None, '00': 0}.get(line[172:174], 1)
        row['numMonthsSinceLastLiveBirth'] = {'999':None, '888':None}.get(line[197:200], line[197:200])
        row['numMonthsSinceLastOtherPreg'] = {'999':None, '888':None}.get(line[205:208], line[205:208])
        row['numMonthsSinceLastPreg'] = {'999':None, '888':None}.get(line[213:216], line[213:216])

        row['prenatalCareMonthBegan'] = {'00':None, '99':None}.get(line[223:225], line[223:225])
        row['numPrenatalVisits'] = {'99':None}.get(line[237:239], line[237:239])
        row['usedWIC'] = {'Y': 1, 'N': 0, 'U': None}.get(line[250], None)

        row['numDailyCigarettesPriorPreg'] = {'99':None}.get(line[252:254], line[252:254])
        row['numDailyCigarettesFirstTri'] = {'99':None}.get(line[254:256], line[254:256])
        row['numDailyCigarettesSecondTri'] = {'99':None}.get(line[256:258], line[256:258])
        row['numDailyCigarettesThirdTri'] = {'99':None}.get(line[258:260], line[258:260])

        # Risk Factors
        row['prePregDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[312], None)
        row['gestationalDiabetes'] = {'Y': 1, 'N': 0, 'U': None}.get(line[313], None)
        row['prePregHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[314], None)
        row['gestationalHypertension'] = {'Y': 1, 'N': 0, 'U': None}.get(line[315], None)
        row['hypertensionEclampsia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[316], None)
        row['noRiskFactors'] = {'1': 1, '0': 0, '9': None}.get(line[336], None)

        # Infections
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

        # Obstetrics
        row['previousCSection'] = {'Y': 1, 'N': 0, 'U': None}.get(line[330], None)
        row['successfulBreech'] = {'Y': 1, 'N': 0, 'U': None}.get(line[359], None)
        row['failedBreech'] = {'Y': 1, 'N': 0, 'U': None}.get(line[360], None)

        # Labor and Delivery
        row['inductionOfLabor'] = {'Y': 1, 'N': 0, 'U': None}.get(line[382], None)
        row['augmentationOfLabor'] = {'Y': 1, 'N': 0, 'U': None}.get(line[383], None)
        row['steroids'] = {'Y': 1, 'N': 0, 'U': None}.get(line[384], None)
        row['antibiotics'] = {'Y': 1, 'N': 0, 'U': None}.get(line[385], None)
        row['chorioamnionitis'] = {'Y': 1, 'N': 0, 'U': None}.get(line[386], None)
        row['anesthesia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[387], None)
        row['noCharacteristicsOfLabor'] = {'1': 1, '0': 0, '9': None}.get(line[394], None)

        # Method of Delivery
        row['isBreech'] = {'1': 0, '2': 1, '3': 0, '9': None}.get(line[401], None)
        row['isCephalic'] = {'1': 1, '2': 0, '3': 0, '9': None}.get(line[401], None)
        row['usedForceps'] = {'2': 1, '9': None}.get(line[401], 0)
        row['usedVacuum'] = {'3': 1, '9': None}.get(line[401], 0)
        row['wasCSectionDelivery'] = {'1': 0, '2': 1, '9': None}.get(line[407], None)
        row['wasVaginalDelivery'] = {'1': 1, '2': 0, '9': None}.get(line[407], None)

        # Maternal Morbidity
        row['maternalTransfusion'] = {'Y': 1, 'N': 0, 'U': None}.get(line[414], None)
        row['perinealLaceration'] = {'Y': 1, 'N': 0, 'U': None}.get(line[415], None)
        row['rupturedUterus'] = {'Y': 1, 'N': 0, 'U': None}.get(line[416], None)
        row['unplannedHysterectomy'] = {'Y': 1, 'N': 0, 'U': None}.get(line[417], None)
        row['admitToICU'] = {'Y': 1, 'N': 0, 'U': None}.get(line[418], None)
        row['noMorbidity'] = {'1': 1, '0': 0, '9': None}.get(line[426], None)

        # APGAR scores
        row['fiveMinuteAPGAR'] = {'99': None}.get(line[443:445], line[443:445])
        row['tenMinuteAPGAR'] = {'99': None, '88': None}.get(line[447:449], line[447:449])

        row['isTwin'] = {'2': 1}.get(line[453], 0)
        row['isTriplet'] = {'3': 1}.get(line[453], 0)
        row['isQuadruplet'] = {'4': 1}.get(line[453], 0)
        row['isQuintOrHigher'] = {'5': 1}.get(line[453], 0)

        row['isSecondInSet'] = {'2': 1, '9': None}.get(line[458], 0)
        row['isThirdInSet'] = {'3': 1, '9': None}.get(line[458], 0)
        row['isFourthOrHigherInSet'] = {'4': 1, '5': 1, '9': None}.get(line[458], 0)

        row['isMaleBaby'] = {'M':1}.get(line[474], 0)
        row['birthWeightInGrams'] = line[503:507]

        row['numWeeksAtBirthSinceLastPeriod'] = {'99': None}.get(line[489:491], line[489:491])
        row['numWeeksAtBirthObstetricEstimate'] = {'99': None}.get(line[498:500], line[498:500])

        # Abnormal conditons of newborn
        row['assistedVentilationImmediate'] = {'Y': 1, 'N': 0, 'U': None}.get(line[516], None)
        row['assistedVentilationAfter6Hrs'] = {'Y': 1, 'N': 0, 'U': None}.get(line[517], None)
        row['admittedToNICU'] = {'Y': 1, 'N': 0, 'U': None}.get(line[518], None)
        row['surfactant'] = {'Y': 1, 'N': 0, 'U': None}.get(line[519], None)
        row['antibioticsForNewborn'] = {'Y': 1, 'N': 0, 'U': None}.get(line[520], None)
        row['newbornSeizures'] = {'Y': 1, 'N': 0, 'U': None}.get(line[521], None)
        row['noAbnormalNewbornConditions'] = {'1': 1, '0': 0, '9': None}.get(line[530], None)

        # Congenital abnormalities
        row['anencephaly'] = {'Y': 1, 'N': 0, 'U': None}.get(line[536], None)
        row['spinaBifida'] = {'Y': 1, 'N': 0, 'U': None}.get(line[537], None)
        row['congenitalHeartDisease'] = {'Y': 1, 'N': 0, 'U': None}.get(line[538], None)
        row['congenitalHernia'] = {'Y': 1, 'N': 0, 'U': None}.get(line[539], None)
        row['omphalocele'] = {'Y': 1, 'N': 0, 'U': None}.get(line[540], None)
        row['gastroschisis'] = {'Y': 1, 'N': 0, 'U': None}.get(line[541], None)
        row['limbReduction'] = {'Y': 1, 'N': 0, 'U': None}.get(line[548], None)
        row['cleftLip'] = {'Y': 1, 'N': 0, 'U': None}.get(line[549], None)
        row['downSyndrome'] = {'C': 1, 'N': 0, 'P': None, 'U': None}.get(line[551], None)
        row['suspectedChromosomalDisorder'] = {'C': 1, 'N': 0, 'P': None, 'U': None}.get(line[552], None)
        row['hypospadias'] = {'Y': 1, 'N': 0, 'U': None}.get(line[553], None)
        row['noCongenitalAbnormalities'] = {'1': 1, '0': 0, '9': None}.get(line[560], None)

        # Comparable across revisions
        row['diabetesComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1330], None)
        row['chronicHypertensionComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1331], None)
        row['pregHypertensionComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1332], None)
        row['eclampsiaComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1333], None)
        row['usedForcepsComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1334], None)
        row['usedVacuumComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1335], None)
        row['inducedLaborComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1336], None)
        row['wasBreechComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1337], None)
        row['anencephalusComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1339], None)
        row['spinaBifidaComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1340], None)
        row['gastroschisisComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1341], None)
        row['cleftLipComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1342], None)
        row['herniaComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1343], None)
        row['downSyndromeComparable'] = {'1': 1, '2': 0, '9': None}.get(line[1344], None)

        if printedHeader == False:
            print(*row.keys(), sep="\t", file=outPrint)
            printedHeader = True

        print(*row.values(), sep="\t", file=outPrint)
