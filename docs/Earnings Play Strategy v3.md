# **Earnings Play Strategy – Optimized Put Ratio Spread**
*(With Dynamic Buffer Adjustments for Risk Management and Profit Maximization)*  

---

## **Objective**
Execute a **Put Ratio Spread** on **fundamentally strong, sector-leading companies** during **earnings season** to capitalize on:
- **Implied Volatility (IV) crush**
- **Theta decay**
- **Controlled downside exposure**  
while maintaining **a defined risk-reward structure**.

This strategy has been optimized to **maximize profitability** by dynamically adjusting the **buffer size** based on **historical stock movement, IV conditions, and market trends**.

---

## **Step 1: Stock Selection Criteria**
✅ **Sector-Leading Companies**  
- Must be among the **top players in their industry** with a **strong earnings track record**.

✅ **Strong Fundamentals**  
- Look for **consistent EPS growth** and **positive earnings surprises**.  
- **Monitor guidance trends** (bullish or bearish commentary).  

✅ **Liquidity & Option Market Suitability**  
- **Ensure high option liquidity** (tight bid-ask spreads, high open interest).  
- **Avoid low-liquidity stocks**, which can lead to **high slippage and poor fills**.  

✅ **Earnings Move Consideration**  
- **Avoid stocks with extreme post-earnings moves (>10%)** unless IV is **extremely overestimated**.  
- Focus on **stocks with historical post-earnings moves between 4-8%** for better risk control.

---

## **Step 2: Trade Setup – Put Ratio Spread**
📌 **Goal:** Profit from **post-earnings IV crush** and **theta decay** while managing downside risk.  

### **Trade Components**  
- **Buy 1 Put** at a strike price based on the **Expected Move (EM) + dynamic buffer**.  
- **Sell 2 Puts** at a **lower strike price (2-5% below the long put)**.  
- Ensure a **net credit or minimal entry cost** to **reduce margin requirements**.

### **Strike Price Selection – Dynamic Calculation**  
1️⃣ **Calculate Expected Move (EM)**  
   - Retrieve from **options market sources**, OR  
   - Estimate using:  
     ```
     EM = (At-the-Money Call Premium + At-the-Money Put Premium) / Stock Price
     ```
  
2️⃣ **Long Put Strike Calculation (With Dynamic Buffer)**  
   - **Adjust buffer size based on market conditions** (IV Rank & Historical Moves).  
   - Formula:  
     ```
     Long Put Strike = Current Stock Price - (EM + Dynamic Buffer)
     ```

3️⃣ **Short Put Strike Calculation**  
   - Place the **short put 2-5% below the long put**.  
   - If **IV is extremely high**, **widen the spread to avoid assignment risk**.  
   - Formula:  
     ```
     Short Put Strike = Long Put Strike - (2% to 5%)
     ```

---

## **Step 3: Historical Price Movement & Dynamic Buffer Adjustments**
🔍 **Review the past 2 years of post-earnings price action**:  
- **Calculate the minimum, maximum, and average post-earnings moves** across the last 8 earnings releases.  
- If **Max Move > EM + 5%**, widen the strike difference.  

📊 **Dynamic Buffer Adjustments Based on Market Conditions**  
| **Condition**                              | **Buffer Recommendation** |
|-------------------------------------------|---------------------------|
| **IV Rank < 50**                           | **3-5% (Small buffer, capture premium)** |
| **IV Rank 50-70**                          | **5% (Standard buffer, balanced risk-reward)** |
| **IV Rank 70-85**                          | **5-7% (Slightly wider, risk-adjusted)** |
| **IV Rank > 85**                           | **3-5% (Avoid overpricing risk)** |
| **Historical Earnings Move < 5%**          | **3-5% (Tighter, less downside risk)** |
| **Historical Earnings Move 5-7%**          | **5% (Optimal balance)** |
| **Historical Earnings Move 7-10%**         | **7-8% (Increased safety)** |
| **Historical Earnings Move > 10%**         | **8-10% (Higher downside risk protection)** |
| **Stock in Strong Downtrend**              | **7-10% (More protection, conservative)** |
| **Stock in Strong Uptrend (Bullish Bias)** | **3-5% (Less aggressive on the downside)** |

---

## **Step 4: Expiration Date Selection**
📅 **Choose 9-15 Days to Expiration (DTE) for optimal theta decay**.  

🚫 **Avoid weekly expirations before earnings** to **minimize excess IV exposure**.  

📌 **Expiration Selection Based on Market Conditions**:  
- If **stock has a history of fast post-earnings stabilization**, use **9-12 DTE**.  
- If **stock tends to be volatile post-earnings**, extend to **12-15 DTE**.  

---

## **Step 5: When to Enter the Trade**
✅ **Enter the trade 1-3 days before earnings**  
- This allows you to **maximize IV expansion** before the earnings event.  

✅ **Best Entry Timing Based on IV Trends**  
- **If IV Rank is high (above 70)** → **Enter 2-3 days before earnings.**  
- **If IV Rank is moderate (50-70)** → **Enter 1-2 days before earnings.**  
- **If IV Rank is low (<50)** → The trade may be less effective because IV crush won’t be significant.

---

## **Step 6: Post-Earnings Trade Management**
🔍 **Monitor price movement for 1-3 days after earnings** and exit accordingly.

✅ **If Stock Rises Above Long Put** → Sell the long put; let short puts expire worthless.  
✅ **If Stock Nears Long Put Strike** → Monitor for 1-3 days, close if risk increases.  
✅ **If Stock Drops Below Long Put but Above Short Put** → Close trade within 1-3 days.  
✅ **If Stock Falls Below Short Put** → Exit immediately to avoid assignment risk.  

---

## **How to Use This Strategy as a Prompt in ChatGPT**
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

This **enhanced strategy** now **dynamically adjusts risk exposure based on real market behavior**. 🚀 Copy this **detailed prompt** into ChatGPT, and it will generate a fully customized earnings trade setup for you!
