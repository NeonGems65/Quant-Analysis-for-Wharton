import math
import random
import numpy as np
import pandas as pd
import csv
from io import StringIO

metricNames =     ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets", "D/A", "Ebitda Growth", "CF Growth"]
# ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
    # OCF Per Share: TTM-OCF/Shares-Outstanding
# P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

# ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)

stockList = ["NVDA", "INFY", "PLNT"]
stock15yrMetrics = []

for m in range(len(stockList)):
    # netIncmTTM = 0
    # netIncm15yr = 0
    # shEqTTM = 0
    # shEq15yr = 0

    # ocfTTM = 0
    # ocf15yr = 0
    # shOutstTTM = 0
    # shOutst15yr = 9
    # ocfPerShareTTM = 0
    # ocfPerShare15yr = 0
    sharePrice1yravg = 0
    sharePrice15yravg = 0

    # totAssetsTTM = 0
    # totAssets15yr = 0

    # longDebt15yr = 0
    # capex15yr = 0

    # revenue15yr = 0
    # revenueTTM = 0

    # profit15yr = 0
    # profitTTM = 0



    def extract15yrData(k, csv, indexMod):
        dataVal = 0.0
        lengthIterated = 0
        for j in range(csv.loc[k].size - 2):
            
            if lengthIterated < 15 and isinstance(csv.loc[k][j+2+indexMod], str):
                dataVal += float(csv.loc[k][j+2+indexMod].replace(',',""))
                # print(float(csv.loc[k][j+2+indexMod].replace(',',"")))
                lengthIterated += 1
            elif lengthIterated >= 15:
                break
            elif pd.isnull(csv.loc[k][j+2+indexMod]):
                print('nothing will be done')
            else: 
                dataVal += csv.loc[k][j+2+indexMod]
            
        dataVal = dataVal / lengthIterated
        
        return dataVal


    # --------------- Financials CSV ---------------        
    dfFinancials = pd.read_csv('' + stockList[m] +"_annual_financials.csv")

    for i in range(dfFinancials["name"].size):
        
        if (dfFinancials.loc[i]["name"] == "	NetIncome"):
            netIncmTTM = int(dfFinancials.loc[i]['ttm'].replace(',',""))
            netIncm15yr = extract15yrData(i, dfFinancials, 0)
            
        if (dfFinancials.loc[i]["name"] == "TotalRevenue"):
            revenueTTM = int(dfFinancials.loc[i]['ttm'].replace(',',""))
            revenue15yr = extract15yrData(i, dfFinancials, 0)
        
        if (dfFinancials.loc[i]["name"] == "GrossProfit"):
            profitTTM = int(dfFinancials.loc[i]['ttm'].replace(',',""))
            profit15yr = extract15yrData(i, dfFinancials, 0)

    # --------------- Balance Sheet CSV ---------------        

    dfBalance = pd.read_csv('' + stockList[m] +"_annual_balance-sheet.csv")

    for i in range(dfBalance["name"].size):
        
        if (dfBalance.loc[i]["name"] == "TotalAssets"):
            totAssetsTTM = int(dfBalance.loc[i][1].replace(',',""))
            totAssets15yr = extract15yrData(i, dfBalance, 0)

        if (dfBalance.loc[i]["name"] == "	StockholdersEquity"):
            shEqTTM = int(dfBalance.loc[i][1].replace(',',""))
            shEq15yr = extract15yrData(i, dfBalance,0)
            
        if (dfBalance.loc[i]["name"] == "ShareIssued"):
            shOutstTTM = int(dfBalance.loc[i][1].replace(',',""))
            shOutst15yr = extract15yrData(i, dfBalance,0)
        
        if (dfBalance.loc[i]["name"] == "			LongTermDebt"):
            longDebt15yr = extract15yrData(i, dfBalance, 0)
            
    # --------------- Cash Flow CSV ---------------        
    with open('' + stockList[m] + '_annual_cash-flow.csv', 'r') as file:
        csv_content = file.read()

    # Replace non-breaking spaces with regular spaces
    csv_content = csv_content.replace('\xA0', ' ')
    dfCashFlow = pd.read_csv(StringIO(csv_content))
    print(dfCashFlow)
    for i in range(dfCashFlow["name"].size):
        print(dfCashFlow)
        if (dfCashFlow.loc[i]["name"] == "OperatingCashFlow"):
            ocfTTM = int(dfCashFlow.loc[i][1].replace(',',""))
            ocf15yr = extract15yrData(i, dfCashFlow, 0)
            
        if (dfCashFlow.loc[i]["name"] == "CapitalExpenditure"):
            capex15yr = extract15yrData(i, dfCashFlow, 0)

    # --------------- Share Price CSV ---------------
    dfSharePrice = pd.read_csv('' + stockList[m] +".csv")
    len = dfSharePrice.shape[0]

    for i in range(len):
        if (i < 12):
            # print(dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4])
            sharePrice1yravg += dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4]
            # print(sharePrice1yravg)
        if (i == 11):
            sharePrice1yravg = sharePrice1yravg/12
            
        if (i < 180):
            sharePrice15yravg += dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4]

        if (i == 179):
            sharePrice15yravg = sharePrice15yravg/180


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

    # --------------- Valuation CSV ---------------        
    dfValuation = pd.read_csv('' + stockList[m] +"_annual_valuation_measures.csv")

    for i in range(dfValuation["name"].size):
        
        if (dfValuation.loc[i]["name"] == "PeRatio"):
            pe15yr = extract15yrData(i, dfValuation, 0)
            print(pe15yr)
        if (dfValuation.loc[i]["name"] == "PsRatio"):
            ps15yr = extract15yrData(i, dfValuation, 0)
        
        if (dfValuation.loc[i]["name"] == "PbRatio"):
            pb15yr = extract15yrData(i, dfValuation, 0)
        
        if (dfValuation.loc[i]["name"] == "EnterprisesValueEBITDARatio"):
            evEbtida15yr = extract15yrData(i, dfValuation, 0)
            evEbitdaTTM = float(dfValuation.loc[i][1].replace(',',""))
    # ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
        # OCF Per Share: TTM-OCF/Shares-Outstanding
    # P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

    # ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)


    roe15yr = netIncm15yr / shEq15yr
    roa15yr = netIncm15yr / totAssets15yr

    rod15yr = netIncm15yr / longDebt15yr
    roi15yr = netIncm15yr / capex15yr


    # ocfPerShareTTM = ocfTTM/shOutstTTM
    ocfPerShare15yr = ocf15yr/shOutst15yr
    # pcfTTM = sharePrice1yravg / ocfPerShareTTM
    pcf15yr = sharePrice15yravg / ocfPerShare15yr

    print("profit")
    print(profitTTM)
    print(profit15yr)
    revenueGrowth15yr = (revenueTTM - revenue15yr) / revenue15yr
    equityGrowth15yr = (shEqTTM - shEq15yr) / shEq15yr
    profitGrowth15yr = (profitTTM - profit15yr) / profit15yr
    assetsGrowth15yr = (totAssetsTTM - totAssets15yr) / totAssets15yr

    print('long debt')
    debtToAssets = (longDebt15yr/totAssets15yr)

    ebitdaGrowth15yr = (evEbitdaTTM - evEbtida15yr) / evEbtida15yr
    cfGrowth15yr = (ocfTTM - ocf15yr) / ocf15yr
    
    metrics = [pe15yr, evEbtida15yr, pb15yr, pcf15yr, ps15yr, roe15yr, roa15yr, rod15yr, roi15yr, revenueGrowth15yr, profitGrowth15yr, equityGrowth15yr, assetsGrowth15yr, debtToAssets, ebitdaGrowth15yr, cfGrowth15yr ]
    stock15yrMetrics.append(metrics)

fileName = "all_metrics.csv"
with open(fileName, 'w', newline="") as f:
    csvWriter = csv.writer(f)
    
    csvWriter.writerow(metricNames)
    for metrics in stock15yrMetrics:
        csvWriter.writerow(metrics)
