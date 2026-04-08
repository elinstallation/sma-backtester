import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import pandas as pd
import main 

fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(top=0.8, bottom=0.15)

def plot_logic(company):

    company = company.upper()

    ax.clear()

    data = main.run_backtest(company)

    ax.plot(data["market_return"], label="Market (Buy & Hold)")
    ax.plot(data["strategy_return"], label = "Strategy")
    ax.set_title(f"Results for: {company}")
    ax.legend()
    plt.draw()

axbox = plt.axes([0.3, 0.85, 0.4, 0.05])
text_box = TextBox(axbox, "Search Company", initial="AAPL")

text_box.on_submit(plot_logic)
plot_logic("AAPL")
plt.show()