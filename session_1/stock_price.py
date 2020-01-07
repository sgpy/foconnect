from matplotlib import pyplot as plt
import pandas as pd

stock_codes = ['AAPL', 'BAC', 'GOOG', 'TSLA']

prices = [pd.read_csv('session_1/prices/{}.csv'.format(s))
          for s in stock_codes]

monthly_avg = [p.groupby(p.Date.str[:7])['Adj Close'].mean() for p in prices]

plt.suptitle('Share price performance over the last 12 months')

for idx, p in enumerate(monthly_avg):
    plt.subplot(2, 2, idx + 1)
    plt.plot(monthly_avg[idx])
    plt.ylabel(stock_codes[idx])
    plt.xticks(rotation=45, ha='right')

plt.show()
