'''
10/17- first one outputted by ai

TODO
- create another ai to check their work and add in missing funcs
'''

import backtesting

# Define the trading strategy
def strategy(signal):
    # Implement the entry conditions
    if signal['VWAP'] > signal['VWAP_365_days_ago']:
        buy = True
    elif signal['volume_spike'] and signal['price_increase']:
        buy = True
    elif signal['positive_news']:
        buy = True
    elif signal['positive_sentiment']:
        buy = True
    elif signal['bullish_trend']:
        buy = True
    elif signal['approaching_support_level']:
        buy = True
    else:
        buy = False

    # Implement the exit conditions
    if signal['approaching_resistance_level']:
        sell = True
    else:
        sell = False

    return buy, sell

# Create a backtesting instance
bt = backtesting.Backtest(strategy)

# Run the backtest on BTC-USD market data
bt.run("BTC-USD")

# Print the results
bt.print_results()