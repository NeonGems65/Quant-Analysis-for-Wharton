import math
import random
import numpy as np
import csv
metricNames =     ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
baseMetricVals = [  0.54,  0.46,        0.63 , 0.56,   0.88,  150.00, 48.85,            1, 1, 1,      1,   1,      1, ]
possibilityMatrices = []
oScoreArr = []

pe15yr = 39.58
evEbtida15yr = 29.86
pb15yr = 32.55
pcf15yr = 40.67
ps15yr = 17.25
roe15yr = 0.9338
roa15yr = 0.2880
rod15yr = 1.9659
roi15yr = 0.5224
rev15yr = 0.8841
prf15yr = 0.5412
eqi15yr = 0.6126
ast15yr = 0.4885


numPossibilities = 1000
for i in range(numPossibilities):
    total = 0.0
    amnt = .38
    
    peMod = 0.000001
    evEbitdaMod = 0.000001
    pbMod = 0.000001
    pcfMod = 0.000001
    psMod = 0.000001
    roeMod = 0.000001
    roaMod = 0.000001
    rodMod = 0.000001
    roiMod = 0.000001
    revenueMod = 0.000001
    profitMod = 0.000001
    equityMod = 0.000001
    assetsMod = 0.000001
    
    while True:
        
        min = 0.001
        index = random.randint(0, len(metricNames) - 1) 
        
        if metricNames[index] == 'P/E':
            peMod = random.uniform(min, amnt)
            total += peMod
            amnt -= peMod
            
        
        elif metricNames[index] == 'EV/EBITDA':
            evEbitdaMod = random.uniform(min, amnt)
            total += evEbitdaMod
            amnt -= evEbitdaMod
        
        elif metricNames[index] == 'P/B':
            pbMod = random.uniform(min, amnt)
            total += pbMod
            amnt -= pbMod
            
        elif metricNames[index] == 'P/CF':
            pcfMod = random.uniform(min, amnt)
            total += pcfMod
            amnt -= pcfMod
        
        elif metricNames[index] == 'P/S':
            psMod = random.uniform(min, amnt)
            total += psMod
            amnt -= psMod
            
        elif metricNames[index] == 'ROE':
            roeMod = random.uniform(min, amnt)
            total += roeMod
            amnt -= roeMod
        
        elif metricNames[index] == 'ROA':
            roaMod = random.uniform(min, amnt)
            total += roaMod
            amnt -= roaMod
        
        elif metricNames[index] == 'ROD':
            rodMod = random.uniform(min, amnt)
            total += rodMod
            amnt -= rodMod  
            
        elif metricNames[index] == 'ROI':
            roiMod = random.uniform(min, amnt)
            total += roiMod
            amnt -= roiMod    
            
        elif metricNames[index] == 'Revenue':
            revenueMod = random.uniform(min, amnt)
            total += revenueMod
            amnt -= revenueMod
            
        elif metricNames[index] == 'Profit':
            profitMod = random.uniform(min, amnt)
            total += profitMod
            amnt -= profitMod
            
        elif metricNames[index] == 'Equity':
            equityMod = random.uniform(min, amnt)
            total += equityMod
            amnt -= equityMod
            
        elif metricNames[index] == 'Assets':
            assetsMod = random.uniform(min, amnt)
            total += assetsMod
            amnt -= assetsMod

               
        metricNames.pop(index)
        print(total)

        if 0.375 <= total <= .38:
            metricNames =  ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
            break
            

    possibilityMatrix = []
    for  i in range(len(baseMetricVals)):
        
        if (metricNames[i] == "P/E"):
            pe = baseMetricVals[i] / peMod
            pe = ((pe15yr/pe) * (1/13))
            possibilityMatrix.append(pe)


        if (metricNames[i] == "EV/EBITDA"):
            evEbitda = baseMetricVals[i] / evEbitdaMod
            evEbitda = ((evEbtida15yr/evEbitda) * (1/13))
            possibilityMatrix.append(evEbitda)

        if (metricNames[i] == "P/B"):
            pb = baseMetricVals[i] / pbMod
            pb = ((pb15yr/pb) * (1/13))
            possibilityMatrix.append(pb)

        if (metricNames[i] == "P/CF"):
            pcf = baseMetricVals[i] / pcfMod
            pcf = ((pcf15yr/pcf) * (1/13))
            possibilityMatrix.append(pcf)

        if (metricNames[i] == "P/S"):
            ps = baseMetricVals[i] / psMod
            ps = ((ps15yr/ps) * (1/13))
            possibilityMatrix.append(ps)

        if (metricNames[i] == "ROE"):
            roe = roeMod / baseMetricVals[i]
            roe = ((roe/roe15yr) *  (1/13))
            possibilityMatrix.append(roe)

        if (metricNames[i] == "ROA"):
            roa = roaMod / baseMetricVals[i]
            roa = ((roa/roa15yr) *  (1/13))
            possibilityMatrix.append(roa)

        if (metricNames[i] == "ROD"):
            rod = rodMod / baseMetricVals[i]
            rod = ((rod/rod15yr) *  (1/13))
            possibilityMatrix.append(rod)

        if (metricNames[i] == "ROI"):
            roi = roiMod / baseMetricVals[i]
            roi = ((roi/roi15yr) *  (1/13))
            possibilityMatrix.append(roi)

        if (metricNames[i] == "Revenue"):
            revenue = revenueMod / baseMetricVals[i]
            revenue  = ((revenue/rev15yr) *  (1/13))
            possibilityMatrix.append(revenue)

        if (metricNames[i] == "Profit"):
            profit = profitMod / baseMetricVals[i]
            profit = ((profit/prf15yr) *  (1/13))
            possibilityMatrix.append(profit)

        if (metricNames[i] == "Equity"):
            equity = equityMod / baseMetricVals[i]
            equity = ((equity/eqi15yr) *  (1/13))
            possibilityMatrix.append(equity)

        if (metricNames[i] == "Assets"):
            assets = assetsMod / baseMetricVals[i]
            assets = ((assets/ast15yr) *  (1/13))
            possibilityMatrix.append(assets)

    possibilityMatrices.append(possibilityMatrix)
    oScoreArr.append(math.fsum(possibilityMatrix))


    
print(oScoreArr)

with open('O-Scores.csv', 'w', newline="") as f:
    csvWriter = csv.writer(f)
    for score in oScoreArr:
        csvWriter.writerow([score])    
    print("DONe")