import sys
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.append(str(Path(__file__).parent.parent))

from config import setting_binance

# Uso
symbol = setting_binance.SYMBOL
start_date = setting_binance.START_STR
end_date = setting_binance.END_STR

print(symbol, start_date, end_date)