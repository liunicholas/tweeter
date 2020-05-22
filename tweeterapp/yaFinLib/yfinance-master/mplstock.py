from yfinance import *
import matplotlib.pyplot as plt, mpld3
import pandas as pd

from datetime import datetime
from matplotlib.dates import DateFormatter

stock = Ticker("spy")
hist = stock.history(period="max")

openList = []
closeList = []
dateList = []
for i in range(hist.shape[0]):
    line = hist.iloc[i]
    openList.append(line["Open"])
    closeList.append(line["Close"])
    dateList.append([hist.index[i].year,hist.index[i].month,hist.index[i].day])

# myDates = [datetime(dateList[0][0],dateList[0][1],dateList[0][2]) for i in range(len(dateList))]
# fig, ax = plt.subplots()
# ax.plot(myDates,openList)
#
# myFmt = DateFormatter("%d")
# ax.xaxis.set_major_formatter(myFmt)

## Rotate date labels automatically
# fig.autofmt_xdate()
# date = "\'"+str(dateList[0][0])+"/"+str(dateList[0][1])+"/"+str(dateList[0][2])+"\'"
# ts = pd.Series(openList, index=pd.date_range(date, periods=len(dateList)))
# ts.cumsum()
# ts.plot()

# plt.plot(openList)
# mpld3.show()

# fig = plt.figure()
# # print(type(fig))
# plot = plt.plot(openList)
# fig.add_subplot(plot)
# fig.show()

fig, ax = plt.subplots()
ax.plot(openList)
print(type(fig))


# mpld3.show()
# graph = fig_to_html()
# context['graph'] = graph
