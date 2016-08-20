# -*- coding: utf-8 -*-
import csv
from matplotlib import pyplot as plt
# from matplotlib.font_manager import FontProperties
# font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # header_row_1 = next(reader)
    # for index,column_header in enumerate(header_row):
    #     print index,column_header
    # print(header_row_1)
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[1]))
        lows.append(int(row[3]))

    # print(highs)
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates,highs, c='red',alpha= 0.5)
    plt.plot(dates, lows, c='blue',alpha= 0.5)
    plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)

    # 设置图形的格式
    # plt.title(u"Daily high temperatures黄 , July 2014",fontsize = 24,fontproperties=font_set)
    plt.title("Daily high and low temperatures-2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature(F)" , fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
