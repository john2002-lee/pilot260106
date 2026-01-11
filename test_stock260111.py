import yfinance as yf

msft = yf.Ticker("MSFT")

print("hello world!")
print(msft.info)
hist = msft.history(period ="5d")
print(hist)
#display(hist)

