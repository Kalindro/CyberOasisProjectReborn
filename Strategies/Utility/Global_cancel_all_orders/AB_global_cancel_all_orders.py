from Gieldy.Binance.Manual_initiation.API_initiation_Binance_AB_USDT import API_initiation as API_Binance_AB_USDT
from Gieldy.Kucoin.API_initiation_Kucoin_AB_USDT import API_initiation as API_Kucoin_AB_USDT
from Gieldy.Gateio.API_initiation_Gateio_AB_USDT import API_initiation as API_Gateio_AB_USDT
from Gieldy.Okx.API_initiation_Okx_AB_USDT import API_initiation as API_Okx_AB_USDT
from Gieldy.Huobi.Manual_initiation.API_initiation_Huobi_AB_BTC import API_initiation as API_Huobi_AB_BTC
from Gieldy.Huobi.Manual_initiation.API_initiation_Huobi_AB_ETH import API_initiation as API_Huobi_AB_ETH
from Gieldy.Kucoin.API_initiation_Kucoin_AB_BTC import API_initiation as API_Kucoin_AB_BTC
from Gieldy.Kucoin.API_initiation_Kucoin_AB_ETH import API_initiation as API_Kucoin_AB_ETH
from Gieldy.Refractor_general.Main_refracting import *


def AB_global_cancel_all_orders():
    print("Emergency cancellation of all orders on all ZOBSOLETE_AB exchanges")

    print("Cancelling API_Binance_AB_USDT")
    cancel_all_orders(API_Binance_AB_USDT())
    print("Cancelling API_Kucoin_AB_USDT")
    cancel_all_orders(API_Kucoin_AB_USDT())
    print("Cancelling API_Gateio_AB_USDT")
    cancel_all_orders(API_Gateio_AB_USDT())
    print("Cancelling API_Okex_AB_USDT")
    cancel_all_orders(API_Okx_AB_USDT())
    print("Cancelling API_Huobi_AB_BTC")
    cancel_all_orders(API_Huobi_AB_BTC())
    print("Cancelling API_Huobi_AB_ETH")
    cancel_all_orders(API_Huobi_AB_ETH())
    print("Cancelling API_Kucoin_AB_BTC")
    cancel_all_orders(API_Kucoin_AB_BTC())
    print("Cancelling API_Kucoin_AB_ETH")
    cancel_all_orders(API_Kucoin_AB_ETH())

    print("Emergency cancellation complete")
