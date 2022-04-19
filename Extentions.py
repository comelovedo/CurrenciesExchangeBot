import requests
import json
from Config import keys


class APIException(Exception):
    pass


class CryptoConvector:
    @staticmethod
    def get_price(quote: str, base: str, amount: float):
        if quote == base:
            raise APIException(f'It is not possible to exchange the same currencies {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Unable to process currency {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Unable to process currency  {base}")

        try:
            amount = float(amount)

        except ValueError:
            raise APIException(f'Unable to process the amount {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker] * float(amount)

        return total_base
