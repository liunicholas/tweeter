from yfinance import *

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

import matplotlib.pyplot as plt, mpld3
plt.plot(openList)
# df.plot(kind='scatter',x='',y='Open',color='red')
# plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
mpld3.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import mpld3
# from yfinance import *

# def koch_snowflake(order, scale=10):
#     """
#     Copy-pasted directly from: https://matplotlib.org/gallery/lines_bars_and_markers/fill.html#sphx-glr-gallery-lines-bars-and-markers-fill-py
#     Return two lists x, y of point coordinates of the Koch snowflake.
#     Arguments
#     ---------
#     order : int
#         The recursion depth.
#     scale : float
#         The extent of the snowflake (edge length of the base triangle).
#     """
#     def _koch_snowflake_complex(order):
#         if order == 0:
#             # initial triangle
#             angles = np.array([0, 120, 240]) + 90
#             return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
#         else:
#             ZR = 0.5 - 0.5j * np.sqrt(3) / 3
#
#             p1 = _koch_snowflake_complex(order - 1)  # start points
#             p2 = np.roll(p1, shift=-1)  # end points
#             dp = p2 - p1  # connection vectors
#
#             new_points = np.empty(len(p1) * 4, dtype=np.complex128)
#             new_points[::4] = p1
#             new_points[1::4] = p1 + dp / 3
#             new_points[2::4] = p1 + dp * ZR
#             new_points[3::4] = p1 + dp / 3 * 2
#             return new_points
#
#     points = _koch_snowflake_complex(order)
#     x, y = points.real, points.imag
#     return x, y
#
# x, y = koch_snowflake(order=5)
#
# plt.figure(figsize=(8, 8))
# plt.axis('equal')
# plt.fill(x, y)
# mpld3.show()
