import os
from abc import abstractmethod, ABC

import pandas as pd
import vectorbtpro as vbt

from exchange.get_history import GetFullHistoryDF
from utils.utils import excel_save_formatted_naive


class BacktestTemplate(ABC):
    """Main class with backtesting template"""

    def __init__(self):
        self.vbt_data = None

    @abstractmethod
    def main(self):
        backtest_pickle_name = "backtest.pickle"
        if os.path.exists(backtest_pickle_name):
            pf = vbt.Portfolio.load(backtest_pickle_name)
        else:
            self.vbt_data = self._get_history()
            pf = self.current_strat(vbt_data=self.vbt_data, periods=self.PERIODS)
            pf.save(backtest_pickle_name)
        analytics = pf.stats(agg_func=None)
        trades = pf.get_trade_history()
        print(analytics.to_string())

        try:
            trades[["Index"]] = trades[["Index"]]
            analytics[["Start", "End"]] = analytics[["Start", "End"]]
            if isinstance(trades, pd.DataFrame):
                excel_save_formatted_naive(dataframe=trades, filename="trades_analytics.xlsx")
            if isinstance(analytics, pd.DataFrame):
                excel_save_formatted_naive(dataframe=analytics, filename="backtest_analytics.xlsx")
        except Exception as err:
            print(err)

    @abstractmethod
    def _get_history(self):
        vbt_data = GetFullHistoryDF(pairs_list=self.pairs_list, start=self.START, end=self.END,
                                    timeframe=self.TIMEFRAME, API=self.API, save_load_history=self.SAVE_LOAD_HISTORY,
                                    vol_quantile_drop=self.VOL_QUANTILE_DROP).get_full_history()

        return vbt_data
