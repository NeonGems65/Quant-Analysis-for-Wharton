
import numpy as np
import pandas as pd
import csv
from io import StringIO
import json
import csv
import requests

def get_jsonparsed_data(url):
    response = requests.get(url)
    return response.json()


def getObj(url):
    url = get_jsonparsed_data(url)
    string = json.dumps(url)
    obj = json.loads(string)
    return obj


metricNames =     ['P/E', 'EV/EBITDA', 'P/B', 'P/CF', 'P/S', 'ROE',  'ROA',             "ROD",'ROI',"Revenue", 'Profit', "Equity", "Assets", "D/A", "Ebitda Growth", "CF Growth", "Equity Multiplier"]
# ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
    # OCF Per Share: TTM-OCF/Shares-Outstanding
# P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

# ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)

consumDiscStockList = ["AEO", "AMZN", "ANF", "APTV", "AZO", "BABA", "BBW", "BBY", "BNED", "BURL", "BWA", "CAAS", "CAKE", "CMG", "CZR", "EDU", "ETSY", "FL", "F", "GM", "GRMN", "GRPN", "HAS", "HD", "HMC", "HOG", "HRB", "H", "KMX", "LCII", "LE", "LOW", "LULU", "LVS", "MAR", "MAT", "MCD", "MOV", "M", "NCLH", "NKE", "ORLY", "PLNT", "PTON", "PZZA", "SBUX", "SFIX", "SONY", "SWBI", "TAL", "TCS", "TJX", "TM", "TSLA", "TXRH", "UA", "ULTA", "URBN", "VFC", "VRA", "WEN", "WH", "WSM", "YUM"]
healthStockList = ["ABBV", "ABT", "ACAD", "AMGN", "AMN", "BAX", "BMY", "CI", "CNC", "CPRX", "CVS", "DOC", "GILD", "GMAB", "GMED", "GSK", "HBIO", "ILMN", "IQV", "JNJ", "LQDA", "MCK", "MRK", "MYGN", "NVO", "NVS", "PBH", "PFE", "REGN", "TEVA", "UNH", "VEEV"]
infoTechStockList = ["AAPL", "ACN", "ADBE", "ADI", "ADP", "AEHR", "AMAT", "AMD", "ANET", "ASGN", "ASML", "AVGO", "BILL", "CRM", "CRWD", "CSCO", "CTSH", "DBX", "DELL", "DJCO", "DXC", "FICO", "FTNT", "IBM", "INTC", "INTU", "MANH", "MSFT", "MSI", "NCTY", "NOW", "NVDA", "NXPI", "ORCL", "PANW", "PLTR", "QCOM", "SAP", "SEDG", "SNOW", "TSM", "TXN", "UTSI", "XRX"]
financialsStockList = ["AFL", "ALL", "APAM", "AXP", "BAC", "BAM", "BCS", "BEN", "BLK", "BX", "C", "DB", "DFS", "GBCI", "GEG", "GS", "ICE", "JPM", "KEY", "KKR", "L", "LAZ", "MA", "MCO", "MET", "MS", "MTB", "ONB", "OPY", "OZK", "PNC", "PRU", "PYPL", "RF", "SCHW", "SEIC", "TROW", "UBS", "V", "WFC"]
stockList = ["AAPL"]
stock15yrMetrics = []

keyMetrics = getObj("https://financialmodelingprep.com/api/v3/key-metrics/AAPL?period=annual&apikey=V6J4FVBPQvPyJAWmcPry9kb8pVlTgibE")
for m in range(len(stockList)):
    
    sharePrice1yravg = 0
    sharePrice15yravg = 0



    def extract15yrData(obj, metricName):
        metricVal = 0
        numIterated = 0
        for i in range(len(obj)):
            numIterated += 1
            metricVal += obj[i][metricName]
            
              
        return metricVal


    # --------------- Financials CSV ---------------        
    dfFinancials = getObj("https://financialmodelingprep.com/api/v3/income-statement/"+stockList[m]+"?period=annual&apikey=V6J4FVBPQvPyJAWmcPry9kb8pVlTgibE")
    netIncmAnnual = dfFinancials[0]["netIncome"]
    revenueAnnual = dfFinancials[0]["revenue"]
    profitAnnual = dfFinancials[0]["grossProfit"]
    
    netIncm15yr = extract15yrData(dfFinancials, "netIncome")
    revenue15yr = extract15yrData(dfFinancials, "revenue")
    profit15yr = extract15yrData(dfFinancials, "grossProfit")
    
    print(netIncmAnnual)
    print(revenueAnnual)
    print(profitAnnual)
    print(netIncm15yr)
    print(revenue15yr)
    print(profit15yr)
    # --------------- Balance Sheet CSV ---------------        

    dfBalance = getObj("https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/"+stockList[m]+"?period=annual&apikey=V6J4FVBPQvPyJAWmcPry9kb8pVlTgibE")

    totAssetsAnnual = dfBalance[0]["assets"]
    shEqAnnual = dfBalance[0]["stockholdersequity"]
    shOutstAnnual = dfBalance[0]["commonstocksharesoutstanding"]
    
    totAssets15yr = extract15yrData(dfBalance, "assets")
    shEq15yr = extract15yrData(dfBalance, "stockholdersequity")
    shOutst15yr = extract15yrData(dfBalance, "commonstocksharesoutstanding")
    longDebt15yr = extract15yrData(dfBalance, "longtermdebtnoncurrent")
    
    
        
    
            
    # --------------- Cash Flow CSV ---------------        
    with open('./Information-Technology/' + stockList[m] + '_annual_cash-flow.csv', 'r') as file:
        csv_content = file.read()

    # Replace non-breaking spaces with regular spaces
    csv_content = csv_content.replace('\xA0', ' ')
    dfCashFlow = pd.read_csv(StringIO(csv_content))
    for i in range(dfCashFlow["name"].size):
        if (dfCashFlow.loc[i]["name"] == "OperatingCashFlow"):
            try:
                ocfTTM = int(dfCashFlow.loc[i][1].replace(',',""))
            except AttributeError:
                ocfTTM += dfCashFlow.loc[i][1]
            ocf15yr = extract15yrData(i, dfCashFlow, 0)
            
        if (dfCashFlow.loc[i]["name"] == "CapitalExpenditure"):
            capex15yr = extract15yrData(i, dfCashFlow, 0)

    # --------------- Share Price CSV ---------------
    dfSharePrice = pd.read_csv('./Information-Technology/' + stockList[m] +".csv")
    len = dfSharePrice.shape[0]

    for i in range(len):
        if (i < 252):
            # print(dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4])
            sharePrice1yravg += dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4]
            # print(sharePrice1yravg)
        if (i == 251):
            sharePrice1yravg = sharePrice1yravg/252
            
        if (i < 3780):
            sharePrice15yravg += dfSharePrice.loc[dfSharePrice.shape[0]-1-i][4]

        if (i == 3779):
            sharePrice15yravg = sharePrice15yravg/3780


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
    dfValuation = pd.read_csv('./Information-Technology/' + stockList[m] +"_annual_valuation_measures.csv")

    for i in range(dfValuation["name"].size):
        
        if (dfValuation.loc[i]["name"] == "PeRatio"):
            pe15yr = extract15yrData(i, dfValuation, 0)
        if (dfValuation.loc[i]["name"] == "PsRatio"):
            ps15yr = extract15yrData(i, dfValuation, 0)
        
        if (dfValuation.loc[i]["name"] == "PbRatio"):
            pb15yr = extract15yrData(i, dfValuation, 0)
        
        if (dfValuation.loc[i]["name"] == "EnterprisesValueEBITDARatio"):
            evEbtida15yr = extract15yrData(i, dfValuation, 0)
            
            if pd.isnull(dfValuation.loc[i][1]):
                print('nothing will be done')
                evEbitdaTTM = 0
            else:
                evEbitdaTTM = float(dfValuation.loc[i][1].replace(',',""))
    # ROE: [(TTM Net Income/ TTM Shareholder Equity) - (15yrPast Net Income/ 15yrPast Shareholder Equity)] / (15yrPast Net Income/ 15yrPast Shareholder Equity)
        # OCF Per Share: TTM-OCF/Shares-Outstanding
    # P/CF: Share-Price (30 day avg) / OCF Per Share **If Share Price not available, another formula: https://www.investopedia.com/terms/p/price-to-cash-flowratio.asp

    # ROA: [(TTM Net Income/TTM Total Assets) - (15yrPast Net Income/15yrPast Total Assets)] / (15yrPast Net Income/15yrPast Total Assets)

    roe15yr = netIncm15yr / shEq15yr
    roa15yr = netIncm15yr / totAssets15yr
    
    print(stockList[m])
    try:
        rod15yr = netIncm15yr / longDebt15yr
    except ZeroDivisionError:
        rod15yr = netIncm15yr / 1
    roi15yr = netIncm15yr / capex15yr


    # ocfPerShareTTM = ocfTTM/shOutstTTM
    ocfPerShare15yr = ocf15yr/shOutst15yr
    # pcfTTM = sharePrice1yravg / ocfPerShareTTM
    pcf15yr = sharePrice15yravg / ocfPerShare15yr

    revenueGrowth15yr = (revenueTTM - revenue15yr) / revenue15yr
    equityGrowth15yr = (shEqTTM - shEq15yr) / shEq15yr
    profitGrowth15yr = (profitTTM - profit15yr) / profit15yr
    assetsGrowth15yr = (totAssetsTTM - totAssets15yr) / totAssets15yr

    debtToAssets = (longDebt15yr/totAssets15yr)
 
    try:
        ebitdaGrowth15yr = (evEbitdaTTM - evEbtida15yr) / evEbtida15yr
    except ZeroDivisionError:
        ebitdaGrowth15yr = 0
    except NameError:
        ebitdaGrowth15yr = 0

    cfGrowth15yr = (ocfTTM - ocf15yr) / ocf15yr
    equityMult = totAssets15yr / shEq15yr
    
    metrics = [pe15yr, evEbtida15yr, pb15yr, pcf15yr, ps15yr, roe15yr, roa15yr, rod15yr, roi15yr, revenueGrowth15yr, profitGrowth15yr, equityGrowth15yr, assetsGrowth15yr, debtToAssets, ebitdaGrowth15yr, cfGrowth15yr, equityMult ]
    stock15yrMetrics.append(metrics)

fileName = "all_metrics.csv"
with open(fileName, 'w', newline="") as f:
    csvWriter = csv.writer(f)
    
    header_row = ["Stock"] + metricNames
    csvWriter.writerow(header_row)
    
    for i, metrics in enumerate(stock15yrMetrics):
        # Write the stock name and the corresponding metrics
        row = [stockList[i]] + metrics
        csvWriter.writerow(row)
print("FINISHED")