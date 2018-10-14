import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import requests
import json
#import marquee.py

assets = pd.DataFrame.from_csv("marquee_companies.csv")
#data = pd.DataFrame.from_csv("sample.csv")

for i in assets.ticker:
    print("\""+ i + "\", ")
#
# col = ['growthScore','financialReturnsScore','multipleScore','integratedScore']
# for i in range(3):
#     X = data['date'][i*(130):(i+1)*130]
#     Y1 = data[col[0]][i*(130):(i+1)*130]
#     Y2 = data[col[1]][i*(130):(i+1)*130]
#     Y3 = data[col[2]][i*(130):(i+1)*130]
#     Y4 = data[col[3]][i*(130):(i+1)*130]
#     plt.plot(X,Y1)
#     plt.plot(X,Y2)
#     plt.plot(X,Y3)
#     plt.plot(X,Y4)
#     plt.legend(col,loc = 'best')
#     plt.xticks(np.arange(0,len(X),15))
#     plt.title("%s stock scores from %s to %s" % (data['ticker'][i*130], data['date'][i*130],
#     data['date'][(i+1)*130-1]))
#     plt.show()
