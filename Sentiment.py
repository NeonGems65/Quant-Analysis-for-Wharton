import json
import csv
import urllib.request

txtfile = open('output.txt', 'w')

def get_jsonparsed_data(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        return json.loads(data.decode())

def getObj(url):
    return get_jsonparsed_data(url)

# Attain APIKey from this website https://www.alphavantage.co/support/#api-key and paste into string
# apiKey = "0K6Z1IRED41VX9RS"
# apiKey = "FRUP33ILUMVIJFAI"
# apiKey = "31OWSPTVLBN8K6LX"
apiKey = "W8S3IOCJ9J711O6I"
# apiKey = "IWZMEW5TR1MDQANT"

# Set start and end date for "past" analysis
startDate1 = "20240901T0130"
endDate1 = "20241201T0130"

# Set 2nd start date, will collect data all the way to the present
startDate2 = "20250104T0130"

# List of tickers that will be analyzed
listOfTickers = ["CZR", "SONY", "TSLA", "LAZ", "MS", "UBS", "ILMN", "IQV", "ASML", "MSFT", "NOW", "NVDA"]
    # listOfTickers = ["NVDA", "ORIS"]
    # listOfTickers = ["VCR","VFH","SMH","VGT","QQQ","SCHD","SPY","VONG"]

txtfile.write("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=" + "NVDA" + "&limit=1000&time_from=" + startDate1 + "&time_to=" + endDate1 + "&apikey=" + apiKey)
def generateCsvs(selectedTicker):
    
    
    ## Time from Sept 2024 to Dec 2024
    pastObj = getObj("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=" + selectedTicker + "&limit=1000&time_from=" + startDate1 + "&time_to=" + endDate1 + "&apikey=" + apiKey)
    ## Time from Jan 2025 to present
    presentObj = getObj("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=" + selectedTicker + "&limit=1000&time_from=" + startDate2 + "&apikey=" + apiKey)
    
    def findSentAvg(tickerSymbol, obj):
            j = 0
            sentScoreAvg = 0.0
            for item in obj["feed"]:
                print(selectedTicker)
                for ticker in item["ticker_sentiment"]:
                    if ticker["ticker"] == tickerSymbol:
                        sentScoreAvg += float(ticker["ticker_sentiment_score"])
                        j += 1
            if j == 0:
                return 0.0, 0  # Prevent division by zero
            sentScoreAvg /= j
            return sentScoreAvg, j
    
    def generateResult(obj, nameOfFile):
        print(obj)
        # tickerList = []
        # for item in obj["feed"]:
        #     for ticker_sentiment in item["ticker_sentiment"]:
        #         newTicker = ticker_sentiment["ticker"]
        #         if newTicker not in tickerList:
        #             tickerList.append(newTicker)
        # tickerList.sort()
        #txtfile.write(tickerList)
        
        #sentScoreList = []
        #ratingsFound = []
        verbalRating = ""
        
        # for ticker in tickerList:
            
        # if ticker == selectedTicker: 
        sentScoreAvg, j = findSentAvg(selectedTicker, obj)
        #txtfile.write(ticker)
        #txtfile.write(sentScoreAvg)
        #sentScoreList.append(sentScoreAvg)
        ratingsFound = j
                
        if sentScoreAvg <= -0.35:
            verbalRating = "Bearish"
        elif -0.35 < sentScoreAvg <= -0.15:
            verbalRating = "Somewhat Bearish"
        elif -0.15 < sentScoreAvg < 0.15:
            verbalRating = "Neutral"
        elif 0.15 <= sentScoreAvg < 0.35:
            verbalRating = "Somewhat Bullish"
        else:
            verbalRating = "Bullish"
        
       ## with open(nameOfFile + "__" + selectedTicker + ".csv", 'w', newline="") as f:
         ##   csvWriter = csv.writer(f)
           ## csvWriter.writerow([selectedTicker, sentScoreAvg, ratingsFound, verbalRating])
        returnArr = [sentScoreAvg, ratingsFound, verbalRating]
        return returnArr
    
    print(selectedTicker)
    
    returnArrPast = generateResult(pastObj, "pastSentiment")
    returnArrPresent = generateResult(presentObj, "presentSentiment")
    return returnArrPast,returnArrPresent



returnArr = []
sentScoreAvgPast = []
ratingsFoundPast = []
verbalRatingPast = []

sentScoreAvgPresent = []
ratingsFoundPresent = []
verbalRatingPresent = []

changeInSentiment = []

for i in range(len(listOfTickers)):
    newSentScoreAvg = 0.0
    newRatingFound = 0
    newVerbalRating = ""
    
    returnArrPast,returnArrPresent = generateCsvs(listOfTickers[i])
   
    sentScoreAvgPast.append(returnArrPast[0])
    ratingsFoundPast.append(returnArrPast[1])
    verbalRatingPast.append(returnArrPast[2])
    
    sentScoreAvgPresent.append(returnArrPresent[0])
    ratingsFoundPresent.append(returnArrPresent[1])
    verbalRatingPresent.append(returnArrPresent[2])
    
    changeInSentiment.append((sentScoreAvgPresent[i] - sentScoreAvgPast[i])/(sentScoreAvgPast[i] + 0.000000001))
    
    txtfile.write("\n" + "Analysis for " + listOfTickers[i]+ "\n")
    txtfile.write(startDate1 + " numerical sentiment: " + str(sentScoreAvgPast[i]) + "\n")
    txtfile.write(startDate1 + " number of ratings found: " + str(ratingsFoundPast[i])+ "\n")
    txtfile.write(startDate1 + " investor sentiment: " + str(verbalRatingPast[i])+ "\n")
    txtfile.write("\n")
    txtfile.write(startDate2 + " numerical sentiment: " + str(sentScoreAvgPresent[i])+ "\n")
    txtfile.write(startDate2 + " number of ratings found: " + str(ratingsFoundPresent[i])+ "\n")
    txtfile.write(startDate2 + " investor sentiment: " + str(verbalRatingPresent[i])+ "\n")
    txtfile.write("\n")
    txtfile.write("Change in sentiment: " + str(changeInSentiment[i] * 100) + "%"+ "\n" )
    txtfile.write("\n")
    txtfile.write("\n")
    
with open("analysis" + ".csv", 'w', newline="") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["Ticker", "Sentiment Score Avg Past", "Sentiment Score Avg Present", "Change in Sentiment (%)", "Investor Sentiment Past", "Investor Sentiment Present", "Ratings Found Past", "Ratings Found Present"])
    for i in range(len(listOfTickers)):
        txtfile.write(str(i))
        txtfile.write(str(ratingsFoundPresent[i]))
        csvWriter.writerow([listOfTickers[i], sentScoreAvgPast[i], sentScoreAvgPresent[i], changeInSentiment[i] * 100, verbalRatingPast[i], verbalRatingPresent[i], ratingsFoundPast[i], ratingsFoundPresent[i]])