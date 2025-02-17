import backtrader as bt

class TestStrategy(bt.Strategy):
    def next(self):
        print("Running Backtest Step")

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)
cerebro.run()
