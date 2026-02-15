import sys
import logging
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from collect import run_bitcoin

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

def run_data_collect() -> None:
    try:
        logger.info("=" * 50)
        logger.info("Iniciando coleta de dados...")
        logger.info("=" * 50)

        # Limpeza dos dados salvos

        # Coleta Bitcoin
        logger.info("Coletando dados históricos do Bitcoin...")
        try:
            run_bitcoin()
            logger.info("✓ Bitcoin coletado com sucesso!")
        except Exception as error:
            logger.error(f"✗ Erro ao coletar Bitcoin: {error}")

        # Outras coletas podem ser adicionadas aqui seguindo o mesmo padrão

        logger.info("=" * 50)
        logger.info("Coleta de dados finalizada!")
        logger.info("=" * 50)

    except Exception as error:
        logger.critical(f"Erro crítico: {error}")
        raise


if __name__ == "__main__":
    run_data_collect()
