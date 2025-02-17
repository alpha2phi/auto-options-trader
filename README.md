# Auto Options Trader

Automated options selling bot using IBKR API.

## Features
✅ Connects to IBKR API (`ib_insync`)  
✅ Fetches real-time option chains  
✅ Executes credit spreads, iron condors based on IV and Delta  
✅ Implements stop-loss and take-profit rules  
✅ Logs trades to a CSV file for tracking  
✅ Includes a backtesting module  

## How to Use
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update `config/config.yaml` with your IBKR credentials.
3. Start the trading bot:
   ```bash
   python main.py
   ```
