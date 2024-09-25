import math
import random
import numpy as np
import pandas as pd
import csv

metricNames =     ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
# ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
    # OCF Per Share: TTM-OCF/Shares-Outstanding
# P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

# ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)



baseMetricVals = [  0.54,  0.46,        0.63 , 0.56,   0.88,  150.00, 48.85,            1, 1, 1,      1,   1,      1, ]
possibilityMatrices = []
oScoreArr = []
pe15yr = 33.402
evEbtida15yr = 15.078
pb15yr = 9.0278
pcf15yr = 30.2425
ps15yr = 5.295
roe15yr = 0.1903
roa15yr = 0.0806
rod15yr = 0.2828
roi15yr = -3.264
rev15yr = 0.748
prf15yr = 0.8509
eqi15yr = 0.7689
ast15yr= 0.8548
ebitdaGrowth = 0.299
cfGrowth = 0.948
eqiMult = 2.148


numPossibilities = 10 
for i in range(numPossibilities):
    print(i)
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
        # print(len(metricNames)-1)

        # If there are metric names left in the list, randomly select one
        if len(metricNames)-1 != -1:
            index = random.randint(0, len(metricNames) - 1) 
        # If there are NO metric names left in the list, re-initliaze all variables and re-assign them
        else:
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
            metricNames =  ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
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
        # print(total)

        if 0.375 <= total <= .38:
            metricNames =  ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
            break
            
            

    possibilityMatrix = []
    for  i in range(len(baseMetricVals)):
        
        if (metricNames[i] == "P/E"):
            pe = ((pe15yr/(prf15yr/peMod))) * (1/13)
            possibilityMatrix.append(pe)
        

        if (metricNames[i] == "EV/EBITDA"):
            evEbitda = ((evEbtida15yr/(ebitdaGrowth/evEbitdaMod))) * (1/13)
            possibilityMatrix.append(evEbitda)
            
        
        if (metricNames[i] == "P/B"):
            pb = (pb15yr) / ((roe15yr*eqi15yr)/pbMod) * (1/13)
            possibilityMatrix.append(pb)
            
        if (metricNames[i] == "P/CF"):
            pcf = (pcf15yr/(cfGrowth/pcfMod)) * (1/13)
            possibilityMatrix.append(pcf)
            
        if (metricNames[i] == "P/S"):
            ps = ((ps15yr/(rev15yr/psMod))) * (1/13)
            possibilityMatrix.append(ps)
            ## Toomuch
        if (metricNames[i] == "ROE"):
            roe = ((eqiMult/roeMod)/roe15yr) * (1/13)
            possibilityMatrix.append(roe)
            
            ## Toomuch
        if (metricNames[i] == "ROA"):
            roa = ((ast15yr/roaMod)/roa15yr) * (1/13)
            possibilityMatrix.append(roa)
            
            
        if (metricNames[i] == "ROD"):
            rod = ((rodMod/rod15yr)) * (1/13)
            possibilityMatrix.append(rod)
            
            
        if (metricNames[i] == "ROI"):
            roi = ((roiMod/roi15yr)) * (1/13)
            possibilityMatrix.append(roi)
           
        if (metricNames[i] == "Revenue"):
            revenue  = ((revenueMod/rev15yr)) * (1/13)
            possibilityMatrix.append(revenue)
            
        if (metricNames[i] == "Profit"):
            profit = ((profitMod/prf15yr)) * (1/13)
            possibilityMatrix.append(profit)
            
        if (metricNames[i] == "Equity"):
            equity = ((equityMod/eqi15yr)) * (1/13)
            possibilityMatrix.append(equity)
            
        if (metricNames[i] == "Assets"):
            assets = ((assetsMod/ast15yr)) * (1/13)
            possibilityMatrix.append(assets)
            print(assets)
    possibilityMatrices.append(possibilityMatrix)
    oScoreArr.append(math.fsum(possibilityMatrix))


    
print(oScoreArr)

with open('O-Scores.csv', 'w', newline="") as f:
    csvWriter = csv.writer(f)
    for score in oScoreArr:
        csvWriter.writerow([score])    
    # print("DONe")
# fileName = stockList[0] + "_metrics.csv"
# with open(fileName, 'w', newline="") as f:
#     csvWriter = csv.writer(f)
#     csvWriter.writerow(metricNames)
#     csvWriter.writerow(stock15yrMetrics)
