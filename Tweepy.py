import tweepy
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def StockChartCreation(ticker, period, start, end):
    # get data on this ticker
    tickerData = yf.Ticker(ticker)

    # get the historical prices for this ticker
    tickerDf = tickerData.history(period=period, start=start, end=end)
    tickerDf.reset_index(inplace=True)
    # Code for Candlestick configuration
    """
    fig = go.Figure(data=[go.Candlestick(x=tickerDf['Date'],
                    open=tickerDf['Open'], high=tickerDf['High'],
                    low=tickerDf['Low'], close=tickerDf['Close'])
                         ])
    """
    fig = go.Figure([go.Scatter(x=tickerDf['Date'], y=tickerDf['High'])])
    # fig.show()
    # fig.update_yaxes(fixedrange=False)
    fig.show()

consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)



for tweet in tweepy.Cursor(api.search, q='doge from:elonmusk').items(10):
    print(tweet.text)
    endDate = tweet.created_at.strftime("%Y-%m-%d")
    print(tweet.created_at)
    startDate=tweet.created_at - timedelta(days=3)
    StockChartCreation('DOGE-USD','1d',startDate.strftime("%Y-%m-%d"), endDate)
#for tweet in tweepy.Cursor(api.user_timeline, id="elonmusk", tweet_mode="extended", include_rts = "False").items(10):
#    print(tweet.created_at.strftime("%Y-%m-%d") + " " + tweet.full_text)