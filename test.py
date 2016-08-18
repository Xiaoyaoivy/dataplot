# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)  # 设置线宽

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of value', fontsize=14)

plt.plot(squares)
plt.show()
