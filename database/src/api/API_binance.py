from binance.client import Client

def get_binance_client():
    """
        Gera o cliente para se conectar a API da Binance

        Return:
            Client: Cliente para se conectar a API
    """
    try:
        return Client()
    
    except Exception as error:
        raise error