import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from config import setting_binance
from api import client_binance

client = client_binance()

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
])[["open_time", "close", "volume"]]


df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
df[["close", "volume"]] = df[["close", "volume"]].astype(float)

print(df.head())


