import pandas_datareader.data as web
import pandas as pd

def fetch_from_web(symbol, start_date, end_date):
    return web.DataReader(symbol, 'yahoo', start_date, end_date)

def get_data(symbols, start_date, end_date):
    """Load daily data from web"""
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = fetch_from_web(symbol, start_date, end_date)[['Adj Close']]
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    return df
