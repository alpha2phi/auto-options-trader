# **Earnings Play Strategy – Optimized Put Ratio Spread**
*(With Dynamic Buffer Adjustments, Risk Hedging, and Execution Enhancements)*

---

## **Objective**

Execute a **Put Ratio Spread** on **fundamentally strong, sector-leading companies** during **earnings season** to capitalize on:

- **Implied Volatility (IV) crush**
- **Theta decay**
- **Controlled downside exposure**  
while maintaining **a defined risk-reward structure** with **enhanced risk mitigation**.

This strategy has been optimized to **maximize profitability** by dynamically adjusting:

- **Buffer size** based on **historical stock movement, IV conditions, and market trends**
- **Put ratio** based on **IV Rank and Expected Move (EM)**
- **Downside protection** via **selective use of deep OTM protective puts**
- **Hedging adjustments based on skew and institutional flow**
- **Automated trade execution using conditional orders**

---

## **Step 1: Stock Selection Criteria**

### ✅ **Sector-Leading Companies**
- Must be among the **top players in their industry** with a **strong earnings track record**.

### ✅ **Strong Fundamentals**
- Look for **consistent EPS growth** and **positive earnings surprises**.
- **Monitor guidance trends** (bullish or bearish commentary).

### ✅ **Liquidity & Option Market Suitability**
- **Ensure high option liquidity** (tight bid-ask spreads, high open interest).
- **Avoid low-liquidity stocks**, which can lead to **high slippage and poor fills**.

### ✅ **Earnings Move Consideration**
- **Avoid stocks with extreme post-earnings moves (>10%)** unless IV is **extremely overestimated**.
- Focus on **stocks with historical post-earnings moves between 4-8%** for better risk control.
- **Check put skew** to assess downside expectations.
- **Monitor short interest**; avoid stocks with >10% short interest due to squeeze risk.
- **Assess institutional order flow** to gauge large trader sentiment.

---

## **Step 2: Trade Setup – Put Ratio Spread**

📌 **Goal:** Profit from **post-earnings IV crush** and **theta decay** while managing downside risk.

### **Trade Components**
- **Buy 1 Put** at a strike price based on the **Expected Move (EM) + dynamic buffer**.
- **Sell 2-3 Puts** at a **lower strike price (2-5% below the long put)**, depending on **IV Rank and risk appetite**.
- Ensure a **net credit or minimal entry cost** to **reduce margin requirements**.

### **Strike Price Selection – Dynamic Calculation**
1. **Calculate Expected Move (EM)**

```
EM = (At-the-Money Call Premium + At-the-Money Put Premium) / Stock Price
```

2. **Long Put Strike Calculation (With Dynamic Buffer)**

```
Long Put Strike = Current Stock Price - (EM + Dynamic Buffer)
```

3. **Short Put Strike Calculation**

```
Short Put Strike = Long Put Strike - (2% to 5%)
```

- **If IV Rank > 85, consider selling 3 puts instead of 2.**
- **If IV is extremely high, widen the spread to avoid assignment risk.**

4. **Protective Put (Optional for High-Risk Scenarios)**
- If **IV Rank > 85** or **historical earnings moves exceed 7%**, buy an **extra OTM put** (10-15% below the short put) for risk hedging.

---

## **Step 3: Historical Price Movement & Dynamic Buffer Adjustments**

📊 **Decision Matrix for Buffer & Ratio Adjustments**

🔍 **Review the past 2 years of post-earnings price action**:  
- **Calculate the minimum, maximum, and average post-earnings moves** across the last 8 earnings releases.  
- If **Max Move > EM + 5%**, widen the strike difference.  


| **Condition**                      | **Buffer Recommendation**                   | **Ratio Adjustment**                  | **Protective Put?**  |
| ---------------------------------- | ------------------------------------------- | ------------------------------------- | -------------------- |
| **IV Rank < 50**                   | **3-5% (Small buffer)**                     | **1:1 (Put Debit Spread)**            | No                   |
| **IV Rank 50-70**                  | **5% (Balanced risk-reward)**               | **1:2 (Standard Ratio Spread)**       | No                   |
| **IV Rank 70-85**                  | **5-7% (More conservative)**                | **1:2 or 1:3**                        | Yes, if EM > 7%      |
| **IV Rank > 85**                   | **3-5% (Avoid overpricing risk)**           | **1:3 (Higher premium capture)**      | Yes, always          |
| **Historical Earnings Move < 5%**  | **3-5% (Tighter risk control)**             | **1:2**                               | No                   |
| **Historical Earnings Move 5-7%**  | **5% (Optimal balance)**                    | **1:2**                               | Yes, if IV Rank > 80 |
| **Historical Earnings Move 7-10%** | **7-8% (Increased safety)**                 | **1:3**                               | Yes, mandatory       |
| **Historical Earnings Move > 10%** | **8-10% (Higher downside risk protection)** | **Avoid trade OR hedge aggressively** | Always               |

---

## **Step 4: Expiration Date Selection**
📅 **Choose 9-15 Days to Expiration (DTE) for optimal theta decay**.

🚫 **Avoid weekly expirations before earnings** to **minimize excess IV exposure**.

📌 **Expiration Selection Based on Market Conditions**:
- **Stable stock post-earnings?** → Use **9-12 DTE**.
- **Volatile stock post-earnings?** → Extend to **12-15 DTE**.

---

## **Step 5: When to Enter the Trade**
✅ **Enter the trade 1-3 days before earnings** to **maximize IV expansion**.

✅ **Best Entry Timing Based on IV Trends**
- **IV Rank > 70** → **Enter 2-3 days before earnings.**
- **IV Rank 50-70** → **Enter 1-2 days before earnings.**
- **IV Rank < 50** → **Avoid trade** (IV crush will be insignificant).

---

## **Step 6: Post-Earnings Trade Management**
🔍 **Monitor price movement for 1-3 days after earnings** and exit accordingly.

✅ **If Stock Rises Above Long Put** → Sell the long put; let short puts expire worthless.  
✅ **If Stock Nears Long Put Strike** → Monitor for 1-3 days, close if risk increases.  
✅ **If Stock Drops Below Long Put but Above Short Put** → Close trade within 1-3 days.  
✅ **If Stock Falls Below Short Put** → Exit immediately to avoid assignment risk.  
✅ **Use trailing stops on long puts to lock in profits.**  
✅ **Consider rolling short puts if IV remains elevated.**  

---

## **How to Use This Strategy in ChatGPT**
Provide the following input for ChatGPT to generate a **specific trade setup**:

```
Stock: [Stock Ticker]
Current Price: [Current Market Price]
Expected Move (EM): [EM % from options market]
IV Rank: [IV Rank Value]
Historical Max Move (Last 8 Earnings): [Highest % Move]
Historical Avg Move (Last 8 Earnings): [Average % Move]
Preferred DTE: [Choose between 9-15 DTE]
```


ChatGPT should return:
✅ **Long Put Strike Based on EM + Dynamic Buffer**  
✅ **Short Put Strike (2-5% below Long Put)**  
✅ **Expiration Selection**  
✅ **Trade Management Guide**  
✅ **Risk Considerations Based on Historical Data**  

---

This **enhanced strategy** now dynamically adjusts for **IV, risk-reward, execution timing, and institutional factors**, ensuring **optimal earnings trading performance**. 🚀
gt