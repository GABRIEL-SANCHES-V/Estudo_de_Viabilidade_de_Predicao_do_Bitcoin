import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from utils import save_in_csv as utils
from config import setting_binance
from api import client_binance

def run_collection_of_historical_bitcoin_data() -> bool:
    """
        Essa função tem como objetivo coletar os dados históricos do Bitcoin utilizando a API da Binance e salvar esses dados em um arquivo CSV. Ela realiza as seguintes etapas:
        
        1. Cria uma instância do cliente da Binance para acessar a API.
        2. Define o diretório onde o arquivo CSV será salvo, utilizando as configurações definidas em `setting_binance`.
        3. Coleta os dados históricos de klines (velas) do Bitcoin para o intervalo de tempo especificado, utilizando os parâmetros definidos em `setting_binance`.
        4. Converte os dados coletados em um DataFrame do Pandas, selecionando apenas as colunas relevantes (tempo de abertura, preço de abertura, preço máximo, preço mínimo, preço de fechamento e volume).
        5. Converte o tempo de abertura para um formato de data e hora legível e os preços e volume para o tipo de dado float.
        6. Salva o DataFrame em um arquivo CSV no diretório especificado.
    """
    try:
        client = client_binance()
        directory = setting_binance.PATH

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

        utils.df_to_csv(dataFrame=df, path=directory)

        return True

    except Exception as error:
        raise error


