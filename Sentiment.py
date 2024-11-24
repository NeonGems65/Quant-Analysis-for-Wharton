import json
import certifi
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

objAAPL = getObj("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=ASML&limit=1000&time_from=20231001T0130&apikey=0K6Z1IRED41VX9RS")
i = 0
tickerList = []
for item in objAAPL["feed"]:

    for ticker_sentiment in item["ticker_sentiment"]:
        newTicker = ticker_sentiment["ticker"]
        found = False

        for ticker in tickerList:
            if newTicker == ticker:
                found = True
        
        if found == False:
            tickerList.append(newTicker)

tickerList.sort()
print(tickerList)


def findSentAvg(tickerSymbol):
    j = 0
    sentScoreAvg = 0.0
    for item in objAAPL["feed"]:
        for ticker in item["ticker_sentiment"]:
            if (ticker["ticker"] == tickerSymbol):
                sentScoreAvg += float(ticker["ticker_sentiment_score"])
                j += 1

    sentScoreAvg /= j
    return sentScoreAvg,j

sentScoreList = []
ratingsFound = []
verbalRating = []

for ticker in tickerList:
    print(ticker)
    sentScoreAvg, j = findSentAvg(ticker)
    print(sentScoreAvg)
    sentScoreList.append(sentScoreAvg)
    ratingsFound.append(j)
    
    if (sentScoreAvg <= -0.35):
        verbalRating.append("Bearish")
    
    elif (sentScoreAvg > -0.35) and (sentScoreAvg <= -0.15):
        verbalRating.append("Somewhat Bearish")
        
    elif (sentScoreAvg > -0.15) and (sentScoreAvg < 0.15):
        verbalRating.append("Neutral")
        
    elif (sentScoreAvg >= 0.15) and (sentScoreAvg < 0.35):
        verbalRating.append("Somewhat Bullish")
        
    elif (sentScoreAvg >= 0.35):
        verbalRating.append("Bullish")
    

# Iterate through the JSON array 
print(sentScoreList)
with open('SentimentScore.csv', 'w', newline="") as f:
    csvWriter = csv.writer(f)
    for i in range(len(tickerList)):
        csvWriter.writerow([tickerList[i]] + [sentScoreList[i]] + [ratingsFound[i]] + [verbalRating[i]])   

