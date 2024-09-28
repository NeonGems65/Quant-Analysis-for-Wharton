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

df = pd.read_csv("Financial Sector Metrics.csv")

sectorMedianIndex = df["Stock"].size - 3

possibilityMatrices = []
stockOScoreArr = []
allStockOScores = []
stockNames = []

numPossibilities = 0
for h in range(df["Stock"].size-3):
    
    stockNames.append(df.loc[h]["Stock"])
    print(stockNames)
    pe15yr = df.loc[h]["P/E"]
    evEbtida15yr = df.loc[h]["EV/EBITDA"]
    pb15yr = df.loc[h]["P/B"]
    pcf15yr = df.loc[h]["P/CF"]
    ps15yr = df.loc[h]["P/S"]
    roe15yr = df.loc[h]["ROE"]
    roa15yr = df.loc[h]["ROA"]
    rod15yr = df.loc[h]["ROD"]
    roi15yr = df.loc[h]["ROI"]
    rev15yr = df.loc[h]["Revenue"]
    prf15yr = df.loc[h]["Profit"]
    eqi15yr = df.loc[h]["Equity"]
    ast15yr= df.loc[h]["Assets"]
    ebitdaGrowth = df.loc[h]["Ebitda Growth"]
    cfGrowth = df.loc[h]["CF Growth"]
    
    numPossibilities = 1000

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
        for  i in range(len(metricNames)):
            

            ## Low = better
            if (metricNames[i] == "P/E"):
                pe = (prf15yr/pe15yr) * peMod
                possibilityMatrix.append(pe)

            ## Low = better
            if (metricNames[i] == "EV/EBITDA"):
                evEbitda = (ebitdaGrowth/evEbtida15yr) * evEbitdaMod
                possibilityMatrix.append(evEbitda)
                
            ## Low = better
            if (metricNames[i] == "P/B"):
                pb = ((roe15yr*eqi15yr)/(pb15yr)) * pbMod
                possibilityMatrix.append(pb)
            
            ## Low = better
            if (metricNames[i] == "P/CF"):
                pcf = (cfGrowth/pcf15yr) * pcfMod
                possibilityMatrix.append(pcf)
            
            ## Low = better
            if (metricNames[i] == "P/S"):
                ps = (rev15yr/ps15yr) * pcfMod
                possibilityMatrix.append(ps)
                
            if (metricNames[i] == "ROE"):
                roe = (roe15yr) * roeMod
                possibilityMatrix.append(roe)
                
            if (metricNames[i] == "ROA"):
                roa = (roa15yr) * roaMod
                possibilityMatrix.append(roa)
                
                
            if (metricNames[i] == "ROD"):
                rod = (rod15yr) * rodMod
                possibilityMatrix.append(rod)
                
                
            if (metricNames[i] == "ROI"):
                roi = (roi15yr) * roiMod
                possibilityMatrix.append(roi)
                
            if (metricNames[i] == "Revenue"):
                revenue  = (rev15yr) * revenueMod
                possibilityMatrix.append(revenue)
                
            if (metricNames[i] == "Profit"):
                profit = (prf15yr) * profitMod
                possibilityMatrix.append(profit)
                
            if (metricNames[i] == "Equity"):
                equity = (eqi15yr) * equityMod
                possibilityMatrix.append(equity)
                
            if (metricNames[i] == "Assets"):
                assets = (ast15yr) * assetsMod
                possibilityMatrix.append(assets)
                
        possibilityMatrices.append(possibilityMatrix)
        stockOScoreArr.append(math.fsum(possibilityMatrix))

    allStockOScores.append(stockOScoreArr)
    
    stockOScoreArr = []
    possibilityMatrices = []


    


with open('Stock-O-Scores.csv', 'w', newline="") as f:
    csvWriter = csv.writer(f)
    
    for i in range(len(allStockOScores)):
        csvWriter.writerow([stockNames[i]] + allStockOScores[i])    
        
    # print("DONe")
# fileName = stockList[0] + "_metrics.csv"
# with open(fileName, 'w', newline="") as f:
#     csvWriter = csv.writer(f)
#     csvWriter.writerow(metricNames)
#     csvWriter.writerow(stock15yrMetrics)
