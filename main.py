import pandas as pd
import numpy as np 

df = pd.read_csv("all_stocks_5yr.csv")

df = df.set_index("date").sort_index()

def run_backtest(company_name):

    df_small = df[df["Name"] == company_name][["close"]].copy()


    df_small["fast_sma"] = df_small["close"].rolling(window=20).mean().dropna()
    df_small["slow_sma"] = df_small["close"].rolling(window=50).mean().dropna()

    df_small.dropna(inplace=True)

    df_small["Signal"] = np.where(df_small["fast_sma"] > df_small["slow_sma"], 1, 0)
    df_small["Position"] = df_small["Signal"].diff()

    trades = df_small[df_small["Position"] != 0]

    market_return = df_small["close"].pct_change()
    strategy_returns = market_return * df_small["Signal"].shift(1)

    df_small["market_return"] = (1 + market_return).cumprod()
    df_small["strategy_return"] = (1 + strategy_returns).cumprod()

    return df_small

#print(df_small[["market_return", "strategy_return"]].iloc[-1])