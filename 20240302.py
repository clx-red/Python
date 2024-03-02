# #算法
# #使用二分法查找e^x = pi 的解
# import numpy as np
# resolution = 0.00001
# def f(x):
#     return np.e ** x - np.pi

# def search(x1,x2):
#     print('Times')
#     x0 = (x1 + x2) / 2
#     if np.abs(f(x0)) <= resolution:
#         print('The solution is:',x0)
#     elif f(x1) * f(x0) < 0:
#         search(x1,x0)
#     elif f(x2) * f(x0) < 0:
#         search(x0,x2)
# search(1,10)
# print('np.log(np.pi) = ',np.log(np.pi))


#建模-曲线拟合
#成年人饮酒后体内酒精含量随时间变化的关系
#时间（h）：[0.25,0.5,0.75,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,12,13,14,15,16]
#酒精含量（mg/100ml）：[30,68,75,82,82,77,68,68,58,51,50,41,38,35,28,25,18,15,12,10,7,7,4]
# import numpy as np
# import matplotlib.pyplot as plt
# time = [0.25,0.5,0.75,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,12,13,14,15,16]
# alcohol = [30,68,75,82,82,77,68,68,58,51,50,41,38,35,28,25,18,15,12,10,7,7,4]
# plt.scatter(time,alcohol,label='sample point')
# plt.xlabel('time(h)')
# plt.ylabel('alcohol(mg/100ml)')
# plt.title('alcohol change with time')
# log_y = [np.log(y) for y in alcohol]
# #print(np.polyfit(time,log_y,1))#一元一次线性拟合[a = -0.16961681 , b = 4.51817704]
# k,b = np.polyfit(time,log_y,1)
# def model(y):
#     return np.e ** (k*y + b)
# time0 = np.linspace(0.25,16,100)#增加采样点
# model_y = [model(y) for y in time0 ]
# plt.plot(time0,model_y,label='ffitting results1')

# sign = alcohol.index(max(alcohol))#找到最大值下标将数据分段
# time2 = time[sign:]
# alcohol2 = alcohol[sign:]
# log_y2 = log_y[sign:]
# k2,b2 = np.polyfit(time2,log_y2,1)
# def model2(y):
#     return np.e ** (k2 * y + b2)
# predy = [model2(y) for y in time2 ]
# plt.plot(time2,predy,label='ffitting results2',c='r')

# #一元二次建模
# a3,b3,c3 = np.polyfit(time,log_y,2)
# def model3(y):
#     return np.e ** (a3 * y**2 + b3*y + c3)
# model_y = [model3(y) for y in time0 ]
# plt.plot(time0,model_y,label='ffitting results13',c='g')

# #效果不显著
# predy = [model3(y) for y in time2 ]
# plt.plot(time2,predy,linestyle='--',label='ffitting results4',c='b')
# plt.legend()
# plt.show()
