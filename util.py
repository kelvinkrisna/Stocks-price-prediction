import warnings
warnings.filterwarnings(action="ignore")

import yfinance as yf
import pandas as pd

def getData(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

df = getData(['PETR4.SA'], '2020-01-01', '2024-12-01')
print(df.head())