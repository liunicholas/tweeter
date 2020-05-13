import yfinance as yf

stock = yf.Ticker("aapl")

# get stock info
this = stock.info

print(this)

# get historical market data
hist = stock.history(period="max")

# show actions (dividends, splits)
stock.actions

# show dividends
stock.dividends

# show splits
stock.splits

# show financials
stock.financials
stock.quarterly_financials

# show major holders
stock.major_holders

# show institutional holders
stock.institutional_holders

# show balance heet
stock.balance_sheet
stock.quarterly_balance_sheet

# show cashflow
stock.cashflow
stock.quarterly_cashflow

# show earnings
stock.earnings
stock.quarterly_earnings

# show sustainability
stock.sustainability

# show analysts recommendations
stock.recommendations

# show next event (earnings, etc)
stock.calendar
