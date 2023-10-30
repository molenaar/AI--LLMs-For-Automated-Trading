# Import necessary libraries
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import talib
import pandas as pd
import numpy as np

# Define the trading strategy class
class MyStrategy(Strategy):

    def init(self):
        # Add any initialization code here for the strategy
        self.long_term_ema = self.I(talib.EMA, timeperiod=365)
        self.short_term_ema = self.I(talib.EMA, timeperiod=30)
        self.rsi = self.I(talib.RSI, timeperiod=14)
        self.macd = self.I(talib.MACD, fastperiod=12, slowperiod=26, signalperiod=9)

    def next(self):
        # Add the trading logic here for the strategy
        if crossover(self.short_term_ema, self.long_term_ema):
            self.buy()
        elif crossover(self.long_term_ema, self.short_term_ema):
            self.sell()

# Load the BTC
