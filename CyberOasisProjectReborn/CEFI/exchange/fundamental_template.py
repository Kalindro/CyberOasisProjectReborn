from abc import ABC
from functools import partial

from CyberOasisProjectReborn.CEFI.API._exchanges_initiator import ExchangeAPISelect
from CyberOasisProjectReborn.CEFI.exchange.exchange_functions import ExchangeFunctions


class FundamentalTemplate(ABC):
    """
    Modes available:
    :EXCHANGE_MODE: 1 - Binance Spot Read; 2 - Binance Futures Read;
                    3 - Bybit Read; 4 - Bybit Trade; 5 - OKX Read; 6 - OKX Trade;
    :PAIRS_MODE: 1 - Test single; 2 - Test multi; 3 - BTC; 4 - USDT
    """

    def __init__(self, exchange_mode: int = None, pairs_mode: int = None):
        if exchange_mode:
            self.API = select_exchange_mode(exchange_mode)
        if pairs_mode:
            self.pairs_list = select_pairs_list_mode(pairs_mode, self.API)


def select_exchange_mode(exchange_mode: int) -> dict:
    """Depending on the PAIRS_MODE, return correct pairs list"""
    exchanges_dict = {1: ExchangeAPISelect().binance_spot_read_only,
                      2: ExchangeAPISelect().binance_futures_read_only,
                      3: ExchangeAPISelect().bybit_read_only,
                      4: ExchangeAPISelect().bybit_trade,
                      5: ExchangeAPISelect().okx_read_only,
                      6: ExchangeAPISelect().okx_trade,
                      }
    exchange = exchanges_dict.get(exchange_mode)
    if exchange is None:
        raise ValueError("Invalid mode: " + str(exchange_mode))
    return exchange()


def select_pairs_list_mode(pairs_mode: int, API: dict) -> list[str]:
    """Depending on the PAIRS_MODE, return correct pairs list"""
    ex = ExchangeFunctions(API)
    pairs_list = {1: partial(ex.get_pairs_list_test_single),
                  2: partial(ex.get_pairs_list_test_multi),
                  3: partial(ex.get_pairs_list_BTC),
                  4: partial(ex.get_pairs_list_USDT),
                  }
    pairs_list = pairs_list.get(pairs_mode)
    if pairs_list is None:
        raise ValueError("Invalid mode: " + str(pairs_mode))
    return pairs_list()
