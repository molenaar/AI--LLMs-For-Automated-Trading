
import backtesting.py as bt

# Create a Strategy
class BitcoinStrategy(bt.Strategy):
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.
from backtesting import Backtest, Strategy 
from backtesting.lib import crossover 
import talib 
import pandas as pd 
import numpy as np 

def hull_ma(data, window):
    weighted_data = 2 * pd.Series(data).ewm(span=window//2).mean() - pd.Series(data).ewm(span=window).mean()
    hull_moving_avg = pd.Series(weighted_data).ewm(span=int(np.sqrt(window))).mean()
    return hull_moving_avg

class HullingMovingAverageStrategy(Strategy):

    hma1 = 20 
    hma2 = 100 

    def init(self):
        self.hma_20 = self.I(hull_ma, self.data.Close, self.hma1)
        self.hma_100 = self.I(hull_ma, self.data.Close, self.hma2)

    def next(self):
        if crossover(self.hma_20, self.hma_100):
           the trading volume of Bitcoin. If the trading volume is increasing, then this could be a good time to buy. If the trading volume is decreasing, then this could be a good time to sell.