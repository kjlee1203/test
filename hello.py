print('hello')
print('2024-01-20')
##################################
import yfinance as yf
import pandas as pd
import numpy as np
df = yf.download("AAPL", start="2020-01-01", end="2020-12-31", progress=False)
df = df.loc[:, ["Adj Close"]]

df["simple_rtn"] = df["Adj Close"].pct_change()
df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))
print(df)