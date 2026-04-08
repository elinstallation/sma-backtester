# SMA Backtester

A simple SMA (Simple Moving Average) crossover strategy backtester for S&P 500 stocks, with an interactive dashboard to visualize results.

## Demo

https://github.com/user-attachments/assets/345e97d4-63ca-49b2-88a2-9a8299600a8f



## What it does

- Implements a **20/50 SMA crossover strategy**: buys when the 20-day SMA crosses above the 50-day SMA, sells when it crosses below
- Compares **strategy returns vs. buy & hold** for any S&P 500 stock
- Provides an **interactive dashboard** where you can search any ticker and instantly see the chart

## Project Structure

```
├── main.py          # Backtesting logic
├── dashboard.py     # Interactive matplotlib dashboard
├── kaggle_api.py    # Script to download the dataset from Kaggle
```

## Setup

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib kagglehub
```

### 2. Download the dataset

The project uses the [S&P 500 stock data](https://www.kaggle.com/datasets/camnugent/sandp500) from Kaggle.

```bash
python kaggle_api.py
```

This will download `all_stocks_5yr.csv` to your project directory.

### 3. Run the dashboard

```bash
python dashboard.py
```

Type any S&P 500 ticker (e.g. `AAPL`, `TSLA`, `MSFT`) into the search box and press Enter to see the results.

## How the strategy works

| Signal | Condition |
|--------|-----------|
| Buy    | 20-day SMA crosses **above** 50-day SMA |
| Sell   | 20-day SMA crosses **below** 50-day SMA |

Returns are calculated daily and compounded to produce the cumulative strategy return, which is plotted against a simple buy & hold benchmark.

## Requirements

- Python 3.7+
- A Kaggle account (for downloading the dataset)
