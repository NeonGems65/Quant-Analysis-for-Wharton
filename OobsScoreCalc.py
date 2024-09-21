import math
import random
import numpy as np
import pandas as pd

metricNames =     ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets"]
# ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
    # OCF Per Share: TTM-OCF/Shares-Outstanding
# P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

# ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)

netIncmTTM = 0
netIncm15yr = 0
shEqTTM = 0
shEq15yr = 0

ocfTTM = 0
shOutst = 0
ocfPerShare = 0
sharePrice30avg = 0

totAssetsTTM = 0
totAssets15yr = 0


def extract15yrData(k, csv, indexMod):
    dataVal = 0
    lengthIterated = 0
    for j in range(15):
        lengthIterated += 1
        dataVal += int(csv.loc[k][j+2+indexMod].replace(',',""))
        print(int(csv.loc[k][j+2+indexMod].replace(',',"")))
        
    print(dataVal)
    dataVal = dataVal / lengthIterated
    print(dataVal)
    
    return dataVal

stockList = ["NVDA"]
# Read the CSV file into a DataFrame
dfFinancials = pd.read_csv('' + stockList[0] +"_annual_financials.csv")

for i in range(dfFinancials["name"].size):
    
    if (dfFinancials.loc[i]["name"] == "	NetIncome"):
        netIncmTTM = int(dfFinancials.loc[i]['ttm'].replace(',',""))
        netIncm15yr = extract15yrData(i, dfFinancials, 0)


dfBalance = pd.read_csv('' + stockList[0] +"_annual_balance-sheet.csv")

for i in range(dfBalance["name"].size):
    
    if (dfBalance.loc[i]["name"] == "TotalAssets"):
        totAssetsTTM = int(dfBalance.loc[i][1].replace(',',""))
        totAssets15yr = extract15yrData(i, dfBalance, 0)
        print(totAssets15yr)

    if (dfBalance.loc[i]["name"] == "	StockholdersEquity"):
        shEqTTM = int(dfBalance.loc[i][1].replace(',',""))
        shEq15yr = extract15yrData(i, dfBalance,0)
        print(shEq15yr)
        
    if (dfBalance.loc[i]["name"] == "ShareIssued"):
        shOutst = int(dfBalance.loc[i][1].replace(',',""))
        
        
dfCashFlow = pd.read_csv('' + stockList[0] +"_annual_cash-flow.csv")

for i in range(dfCashFlow["name"].size):
    if (dfCashFlow.loc[i]["name"] == "OperatingCashFlow"):
        ocfTTM = int(dfCashFlow.loc[i][1].replace(',',""))
        

dfSharePrice = pd.read_csv('' + stockList[0] +".csv")



len = dfSharePrice.shape[0]

for i in range(len):
    if (i < 30):
        # print(dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4])
        sharePrice30avg += dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4]
        # print(sharePrice30avg)
    if (i == 29):
        sharePrice30avg = sharePrice30avg/30



pe15yr = 0
evEbtida15yr = 0
pb15yr = 0
pcf15yr = 0
ps15yr = 0
roe15yr = 0
roa15yr = 0
rod15yr = 0
roi15yr = 0
rev15yr = 0
prf15yr = 0
eqi15yr = 0
ast15yr = 0

dfValuation = pd.read_csv('' + stockList[0] +"_annual_valuation_measures.csv")

for i in range(dfValuation["name"].size):
    
    if (dfValuation.loc[i]["name"] == "PeRatio"):
        pe15yr = extract15yrData(i, dfValuation, 0)
    print(pe15yr)
    
    if (dfValuation.loc[i]["name"] == "PsRatio"):
        ps15yr = extract15yrData(i, dfValuation, 0)
    print(ps15yr)
    
    if (dfValuation.loc[i]["name"] == "PbRatio"):
        pb15yr = extract15yrData(i, dfValuation, 0)
    print(pb15yr)
    
    if (dfValuation.loc[i]["name"] == "EnterprisesValueEBITDARatio"):
        evEbtida15yr = extract15yrData(i, dfValuation, 0)
    print(evEbtida15yr)

# ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
    # OCF Per Share: TTM-OCF/Shares-Outstanding
# P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

# ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)

roe15yr = ((netIncmTTM/shEqTTM) - (netIncm15yr/shEq15yr)) / (netIncm15yr/shEq15yr)
roa15yr = ((netIncmTTM/totAssetsTTM) - (netIncm15yr/totAssets15yr)) / (netIncm15yr/totAssets15yr)

pcf15yr

baseMetricVals = [  0.54,  0.46,        0.63 , 0.56,   0.88,  150.00, 48.85,            1, 1, 1,      1,   1,      1, ]
possibilityMatrices = []
oScoreArr = []

numPossibilities = 0
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
    # print("DONe")