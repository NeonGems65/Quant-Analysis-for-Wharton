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

df = pd.read_csv("Consumer Discretionary Sector Metrics.csv")

sectorMedianIndex = df["Stock"].size - 2

possibilityMatrices = []
oScoreArr = []
pe15yr = df.loc[sectorMedianIndex]["P/E"]
evEbtida15yr = df.loc[sectorMedianIndex]["EV/EBITDA"]
pb15yr = df.loc[sectorMedianIndex]["P/B"]
pcf15yr = df.loc[sectorMedianIndex]["P/CF"]
ps15yr = df.loc[sectorMedianIndex]["P/S"]
roe15yr = df.loc[sectorMedianIndex]["ROE"]
roa15yr = df.loc[sectorMedianIndex]["ROA"]
rod15yr = df.loc[sectorMedianIndex]["ROD"]
roi15yr = df.loc[sectorMedianIndex]["ROI"]
rev15yr = df.loc[sectorMedianIndex]["Revenue"]
prf15yr = df.loc[sectorMedianIndex]["Profit"]
eqi15yr = df.loc[sectorMedianIndex]["Equity"]
ast15yr= df.loc[sectorMedianIndex]["Assets"]
ebitdaGrowth = df.loc[sectorMedianIndex]["Ebitda Growth"]
cfGrowth = df.loc[sectorMedianIndex]["CF Growth"]



# print("MEdian vals")
# print(pe15yr)
# print(roa15yr)
# print(cfGrowth)

numPossibilities = 1000000
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
    # peMod = 0.000001
    # evEbitdaMod = 0.000001
    # pbMod = 0.000001
    # pcfMod = 0.000001
    # psMod = 0.000001
    # roeMod = 0.000001
    # roaMod = 0.000001
    # rodMod = 0.000001
    # roiMod = 0.000001
    # revenueMod = 0.000001
    # profitMod = 0.000001
    # equityMod = 0.000001
    # assetsMod = 0.000001
    for  i in range(len(metricNames)):
        
        

        ## Low = better
            if (metricNames[i] == "P/E"):
                pe = (prf15yr/pe15yr) * peMod
                possibilityMatrix.append(pe)
                # print(pe)
            ## Low = better
            if (metricNames[i] == "EV/EBITDA"):
                evEbitda = (ebitdaGrowth/evEbtida15yr) * evEbitdaMod
                possibilityMatrix.append(evEbitda)
                # print(evEbitda)
            ## Low = better
            if (metricNames[i] == "P/B"):
                pb = ((roe15yr*eqi15yr)/(pb15yr)) * pbMod
                possibilityMatrix.append(pb)
                # print(pb)
            ## Low = better
            if (metricNames[i] == "P/CF"):
                pcf = (cfGrowth/pcf15yr) * pcfMod
                possibilityMatrix.append(pcf)
                # print(pcf)
            ## Low = better
            if (metricNames[i] == "P/S"):
                ps = (rev15yr/ps15yr) * pcfMod
                possibilityMatrix.append(ps)
                # print(ps)
                
            if (metricNames[i] == "ROE"):
                roe = (roe15yr) * roeMod
                possibilityMatrix.append(roe)
                # print(roe)
            if (metricNames[i] == "ROA"):
                roa = (roa15yr) * roaMod
                possibilityMatrix.append(roa)
                # print(roa)
            if (metricNames[i] == "ROD"):
                rod = (rod15yr) * rodMod
                possibilityMatrix.append(rod)
                # print(rod)
            if (metricNames[i] == "ROI"):
                roi = (roi15yr) * roiMod
                possibilityMatrix.append(roi)
                # print(roi)
            if (metricNames[i] == "Revenue"):
                revenue  = (rev15yr) * revenueMod
                possibilityMatrix.append(revenue)
                # print(revenue)
            if (metricNames[i] == "Profit"):
                profit = (prf15yr) * profitMod
                possibilityMatrix.append(profit)
                # print(profit)
            if (metricNames[i] == "Equity"):
                equity = (eqi15yr) * equityMod
                possibilityMatrix.append(equity)
                # print(equity)
            if (metricNames[i] == "Assets"):
                assets = (ast15yr) * assetsMod
                possibilityMatrix.append(assets)
                # print(assets)
    possibilityMatrices.append(possibilityMatrix)
    oScoreArr.append(math.fsum(possibilityMatrix))


    

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
