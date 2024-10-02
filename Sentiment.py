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

objAAPL = getObj("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AMN&limit=100000000000000000&time_from=20090101T0130&apikey=0K6Z1IRED41VX9RS")

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
    return sentScoreAvg

sentScoreList = []
for ticker in tickerList:
    print(ticker)
    print(findSentAvg(ticker))
    sentScoreList.append(findSentAvg(ticker))

# Iterate through the JSON array 
print(sentScoreList)
with open('SentimentScore.csv', 'w', newline="") as f:
    csvWriter = csv.writer(f)
    for i in range(len(tickerList)):
        csvWriter.writerow([tickerList[i]] + [sentScoreList[i]])   

