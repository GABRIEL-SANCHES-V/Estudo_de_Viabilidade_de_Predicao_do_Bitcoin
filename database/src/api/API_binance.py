from binance.client import Client

def get_binance_client():
    """
        Gera o cliente para se conectar a API da Binance

        Return:
            Client: Cliente para se conectar a API
    """

    return Client()