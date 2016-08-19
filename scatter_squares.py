# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# test 1
# plt.scatter(2, 4, s=200)
# plt.axis([1.98,2.020,3.97,4.03])

# test 2
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values, y_values,s=200)  # s为大小

# test 3
x_values = list(range(1, 1001))  # 绘制1000个点
y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values,c= 'red',edgecolor = 'none', s=40)
#增加渐变效果
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Set1,
            edgecolor='none',s=40)
plt.axis([0,1100,0,1100000])

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize='14')

plt.show()
