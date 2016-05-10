from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import util

def calc_sma(prices, window=30):
    return prices['prices'].rolling(window=window).mean()

def calc_bollinger_bands(prices, window=30):
    prices['std'] = prices['prices'].rolling(window=window).std()
    prices['sma'] = calc_sma(prices, window)
    prices['upper_band'] = prices['sma'] + 2 * prices['std']
    prices['lower_band'] = prices['sma'] - 2 * prices['std']
    return prices

def calc_momentum(prices):
    prices['momentum'] = (prices['prices'] / prices['prices'].shift(1) - 1)
    return prices.fillna(0)

def run():
    # Load data
    tickers = ['AAPL', 'TWTR', 'FB']
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2016, 1, 1)

    # data = util.get_data(tickers, start_date, end_date).dropna()
    # data.to_pickle('data.pkl')
    data = util.get_data_from_file('data.pkl')

    # Calculate bollinger bands, sma, momentum
    prices = data['AAPL'].to_frame().rename(columns={'AAPL': 'prices'})
    prices = calc_bollinger_bands(prices)
    prices = calc_momentum(prices)

    # TODO : Discretize data for standarization

    # TODO : Make prediction

    # TODO : Backtest prediction accuracy

if __name__ == '__main__':
    run()
