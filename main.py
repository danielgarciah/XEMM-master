
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: main.py                                                                                       -- #
# -- Description: Main execution logic for the project                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/IFFranciscoME/MarketMaker-BackTest                                   -- #
# --------------------------------------------------------------------------------------------------------- #

# -- Load Packages for this script
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -- Load other scripts
from data import fees_schedule, order_book, get_timeseries, graficar

# Small test
exchanges = ["bitfinex", "kraken", 'ftx', 'currencycom', 'coinmate']
symbol = 'BTC/EUR'
expected_volume = 0

# Get fee schedule
# fees = fees_schedule(exchange='kraken', symbol=symbol, expected_volume=expected_volume)

# Massive download of OrderBook data
#order_book(symbol=symbol, exchanges=exchanges, output='JSON', stop=None, verbose=True)
datos = order_book(symbol=symbol, exchanges=exchanges, output='inplace', stop=None, verbose=True)
pd.DataFrame(datos).to_json('files/Diccionario_series_de_tiempo_BTC_EUR.json')
print(datos)

series = get_timeseries(datos, exchanges)
series.to_excel('files/Dataframe_series_de_tiempo_BTC_EUR.xlsx')
print(series)

graficar(series, exchanges, symbol)

# Cambiando el activo
symbol = 'SOL/USD'
datos = order_book(symbol=symbol, exchanges=exchanges, output='inplace', stop=None, verbose=True)
pd.DataFrame(datos).to_json('files/Diccionario_series_de_tiempo_SOL_USD.json')
print(datos)

series = get_timeseries(datos, exchanges)
series.to_excel('files/Dataframe_series_de_tiempo_SOL_USD.xlsx')
print(series)

graficar(series, exchanges, symbol)

# Cambiando el activo
symbol = 'ETH/USD'
datos = order_book(symbol=symbol, exchanges=exchanges, output='inplace', stop=None, verbose=True)
pd.DataFrame(datos).to_json('files/Diccionario_series_de_tiempo_ETH_USD.json')
print(datos)

series = get_timeseries(datos, exchanges)
series.to_excel('files/Dataframe_series_de_tiempo_ETH_USD.xlsx')
print(series)

graficar(series, exchanges, symbol)

# Read previously downloaded file
#ob_data = pd.read_json('files/orderbooks_06jun2021.json', orient='values', typ='series')
#print(pd.DataFrame(ob_data['kraken']['2021-07-06T19:02:31:692Z']))

# -- Simulation of trades (Pending)

"""
- Type A: Make a BID in Kraken, then Take BID in Bitfinex

Check Signal_BID
    Difference between BIDs on Origin and Destination is greater than Maker_Margin_BID
    Make on Destination and Take on Origin

kr_maker_bid * (1 + kr_maker_fee) = bf_taker_bid * (1 - bf_taker_fee)
e.g. -> 5942.5638 * (1 + 0.0016) = 5964.00 * (1 - 0.0020) = 0

- Type B: Take an ASK on Bitfinex, then Make an ASK in Kraken

Check Signal_ASK
    Difference between ASKs on Origin and Destination is greater than Maker_Margin_ASK
    Take on Origin and Maker on Destination

bf_taker_ask * (1 + bf_taker_fee) = kr_maker_ask * (1 - kr_maker_fee)
e.g. -> 6000 * (1 + 0.0020) - 6021.6346 * (1 - 0.0016) = 0
"""
