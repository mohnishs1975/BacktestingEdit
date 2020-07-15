from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)

    def buy_to_open(self):  
        self.current_price = self.data[GOOG].price
        close_price = self.data.Close
        dev = 0.1 * close_price
        if current_price in range (close_price - dev, close_price + dev):
            number_of_shares = int(cash/current_price)
            self.buy()
        log.info("Buying {} shares at {}".format(number_of_shares, current_price))

    def sell_to_close(self):
        self.current_price = self.data[GOOG].price
        self.sell()
        log.info("Selling shares at {} per share".format(current_price))

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(GOOG, SmaCross,
              cash=10000, commission=.002)
bt.run()
bt.plot()