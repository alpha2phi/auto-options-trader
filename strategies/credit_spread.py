from ib_insync import *

def get_option_chain(symbol, expiry):
    contract = Option(symbol, expiry, 0, 'C', 'SMART')
    chains = ib.reqSecDefOptParams(symbol, '', '', contract.secType)
    chain = next(c for c in chains if c.tradingClass == symbol and c.exchange == "SMART")
    return sorted(chain.strikes)

def sell_put_credit_spread(symbol, expiry, short_delta=-0.30, long_delta=-0.10):
    strikes = get_option_chain(symbol, expiry)
    short_strike = min(strikes, key=lambda s: abs(get_delta(symbol, s, expiry) - short_delta))
    long_strike = min(strikes, key=lambda s: abs(get_delta(symbol, s, expiry) - long_delta))
    
    short_put = Option(symbol, expiry, short_strike, 'P', 'SMART')
    long_put = Option(symbol, expiry, long_strike, 'P', 'SMART')
    
    spread_order = Order('SELL', 1, orderType='LMT', lmtPrice=0.30)
    
    trade = ib.placeOrder([short_put, long_put], spread_order)
    return trade
