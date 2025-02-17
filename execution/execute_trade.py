from ib_insync import *
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def run_trading_bot():
    config = load_config()
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    
    print("Connected to IBKR API")
    
    strategy = config['default_strategy']
    if strategy == "credit_spread":
        from strategies.credit_spread import sell_put_credit_spread
        sell_put_credit_spread("SPY", "20240315")

    ib.disconnect()
