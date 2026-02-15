from . import genaral_configs as config_general

class config_settings_binance:
    """
        Configurações para a API da Binance

        Attributes:
            SYMBOL (str): Símbolo do par de moedas a ser consultado
            START_STR (str): Data de início para consulta dos dados históricos
            END_STR (str): Data de fim para consulta dos dados históricos
            PATH (str): Caminho para salvar os dados históricos em formato CSV
    """
    SYMBOL = "BTCUSDT"
    START_STR = config_general.settings_config_general.START_DATE
    END_STR = config_general.settings_config_general.END_DATE
    PATH = "database/data/bitcoin/bitcoin_historical_data.csv"