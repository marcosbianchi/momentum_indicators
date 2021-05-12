import numpy as np
import pandas as pd
import talib

from binance.client import Client
import os

## initialize connection 
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_momemtum(pair):
    lopen = []
    lclose = []
    lhigh = []
    llow = []
    lvolume = []
    df = pd.DataFrame()
    
    ## obtiene velas del par en el intervalo especificado
    candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_15MINUTE)

    ## Carga los valores de open, high, low, close y volume de cada vela de 1H
    for candle in candles:
        lopen.append(candle[1])
        lhigh.append(candle[2])
        llow.append(candle[3])
        lclose.append(candle[4])
        lvolume.append(candle[5])

    ## Carga los datos en su correspondiente dataframe
    df_close = np.array(lclose).astype(float)
    df_open = np.array(lopen).astype(float)
    df_high = np.array(lhigh).astype(float)
    df_low = np.array(llow).astype(float)
    df_volume = np.array(lvolume).astype(float)

    ## obtiene el RSI 
    RSI = talib.RSI(df_close, timeperiod=14)

    ## obtiene el MFI
    ## MFI(high, low, close, volume, timeperiod=14)
    MFI = talib.MFI(df_high, df_low, df_close, df_volume, timeperiod=14)

    last = len(RSI)
    last = len(MFI)
    if RSI[last-1]>34 and RSI[last-1]<36:
        print(f"{pair:10s} {MFI[last-1]:10.4f} {bcolors.OKGREEN}{RSI[last-1]:10.4}{bcolors.ENDC}")
    else:
        print(f"{pair:10s} {MFI[last-1]:10.4f} {RSI[last-1]:10.4f}")


os.system('clear')

print("{:13s} {:10s} {:10s}".format("Pair","MFI","RSI"))

## Add crypto pairs you want to see here
BTCUSDT = get_momemtum("BTCUSDT")
ADAUSDT = get_momemtum("ADAUSDT")
DOGEUSDT = get_momemtum("ETCUSDT")