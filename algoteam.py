# Import libraries
#import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen, Request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import yfinance as yf
from datetime import date
import finplot as fplt
import requests

page = requests.get('https://www.quandl.com/api/v3/datasets/CHRIS/ICE_OJ1.csv?api_key=9BZrqXiy4Mck8_br9oG9')
print(page.text)
#fplt.candlestick_ochl(df[['Open','Close','High','Low']])
#fplt.show()

