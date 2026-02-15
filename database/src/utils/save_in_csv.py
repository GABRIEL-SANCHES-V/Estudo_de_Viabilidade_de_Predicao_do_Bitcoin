import os
import pandas as pd

def df_to_csv(dataFrame: pd.DataFrame, path: str) -> bool:
    """
        Salva um DataFrame em um arquivo CSV

        Args:
            dataFrame (pd.DataFrame): DataFrame a ser salvo
            path (str): Caminho para salvar o arquivo

        Returns:
            bool: True se o arquivo foi salvo com sucesso, False caso contrário
    """
    try:
        try:
            directory = os.path.dirname(path)
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception as error:
            raise error

        dataFrame.to_csv(path, index=False)
        return True

    except Exception as error:
        raise error