import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from config import setting_binance
from api import client_binance
from utils import save_in_csv as utils

client = client_binance()
path = setting_binance.PATH

klines = client.get_historical_klines(
    symbol=setting_binance.SYMBOL,
    interval=client.KLINE_INTERVAL_1DAY,
    start_str=setting_binance.START_STR,
    end_str=setting_binance.END_STR
)

df = pd.DataFrame(klines, columns=[
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base", "taker_buy_quote", "ignore"
])[["open_time", "open", "high", "low", "close", "volume"]]

df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

utils.df_to_csv(dataFrame=df, path=path)


