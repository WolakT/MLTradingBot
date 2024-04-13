import os

from lumibot.brokers import Ccxt
from lumibot.traders import Trader

# Replace 'your_api_key' and 'your_api_secret' with your actual Binance API key and secret.
trader = Trader()
api_secret = os.environ["BINANCE_SECRET"]
api_key = os.environ["BINANCE_API_KEY"]
BINANCE_CONFIG = {
    "exchange_id": "binance",
    "apiKey": api_key,
    "secret": api_secret,
    "sandbox": True,
    "marigin": False,
}
# Instantiate the Binance broker
broker = Ccxt(BINANCE_CONFIG)
