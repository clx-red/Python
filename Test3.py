# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# np.random.seed(1)
# data = {"name":['name1','name2','name3','name4','name5'],
#         "weight":np.random.randint(55,75,5),
#         "height":np.random.randint(170,200,5),
#         "sagin":[1 for i in range(5)],
#         "grade":np.random.randint(50,100,5)}
# df = pd.DataFrame(data)
# print(df)
# print("average scores:",np.mean(df["grade"]))
# first = df[(df["grade"] == max(df["grade"]))]
# print('The first is:\n',first)
# print("The student(s) who failed:\n", df[(df["grade"] < 60)])
# x = np.linspace(0, 10, 10)
# y = np.sin(x)
# x2 = np.linspace(0, 10, 100)
# y2 = np.sin(x2)
# plt.plot(x2,y2,linestyle='--' ,label="broken line")
# plt.scatter(x,y,marker='.',c='r',label='data point')
# plt.legend()
# plt.title('y = sin(x)')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# # plt.show()
# fig, axes = plt.subplots(2,1)
# axes[0].scatter(x,y,marker='.',c='r',label='data point')
# axes[0].set_title('y = sin(x)')
# axes[0].set_xlabel('x-axis')
# axes[0].set_ylabel('y-axis')
# axes[1].plot(x2,y2,linestyle='--' ,label="broken line")
# axes[1].set_title('y = sin(x)')
# axes[1].set_xlabel('x-axis')
# axes[1].set_ylabel('y-axis')
# fig.legend()
# plt.show()


import numpy as np
# 位置矩阵
coordinates = np.array([[565.0, 575.0], [25.0, 185.0], [345.0, 750.0], [945.0, 685.0], [845.0, 655.0],
                        [880.0, 660.0], [25.0, 230.0], [525.0, 1000.0], [580.0, 1175.0], [650.0, 1130.0],
                        [1605.0, 620.0], [1220.0, 580.0], [1465.0, 200.0], [1530.0, 5.0], [845.0, 680.0],
                        [725.0, 370.0], [145.0, 665.0], [415.0, 635.0], [510.0, 875.0], [560.0, 365.0],
                        [300.0, 465.0], [520.0, 585.0], [480.0, 415.0], [835.0, 625.0], [975.0, 580.0],
                        [1215.0, 245.0], [1320.0, 315.0], [1250.0, 400.0], [660.0, 180.0], [410.0, 250.0],
                        [420.0, 555.0], [575.0, 665.0], [1150.0, 1160.0], [700.0, 580.0], [685.0, 595.0],
                        [685.0, 610.0], [770.0, 610.0], [795.0, 645.0], [720.0, 635.0], [760.0, 650.0],
                        [475.0, 960.0], [95.0, 260.0], [875.0, 920.0], [700.0, 500.0], [555.0, 815.0],
                        [830.0, 485.0], [1170.0, 65.0], [830.0, 610.0], [605.0, 625.0], [595.0, 360.0],
                        [1340.0, 725.0], [1740.0, 245.0]])
# 点的总数量
num = coordinates.shape[0]
# 两点之间的距离矩阵
distance = np.zeros((num, num))
for i in range(num):
    for j in range(i, num):
        distance[i][j] = distance[j][i] = np.linalg.norm(coordinates[i] - coordinates[j])
# 三大超参数
delta = 0.99
t = 100
tk = 1

solution_new = np.arange(num)
solution_current = solution_new.copy()
value_current = 99000  # np.max这样的源代码可能同样是因为版本问题被当做函数不能正确使用，应取一个较大值作为初始值
solution_best = solution_new.copy()
value_best = 99000  # np.max
result = []  # 记录迭代过程中的最优解
while t > tk:
    for i in np.arange(1000):
        # 下面的两交换和三角换是两种扰动方式，用于产生新解
        if np.random.rand() > 0.5:  # 交换路径中的这2个节点的顺序
            while True:  # 产生两个不同的随机数
                loc1 = int(np.ceil(np.random.rand() * (num - 1)))
                loc2 = int(np.ceil(np.random.rand() * (num - 1)))
                if loc1 != loc2:
                    break
            solution_new[loc1], solution_new[loc2] = solution_new[loc2], solution_new[loc1]
        else:  # 三交换
            while True:
                loc1 = int(np.ceil(np.random.rand() * (num - 1)))
                loc2 = int(np.ceil(np.random.rand() * (num - 1)))
                loc3 = int(np.ceil(np.random.rand() * (num - 1)))
                if (loc1 != loc2) & (loc2 != loc3) & (loc1 != loc3):
                    break
            # 下面的三个判断语句使得loc1<loc2<loc3
            if loc1 > loc2:
                loc1, loc2 = loc2, loc1
            if loc2 > loc3:
                loc2, loc3 = loc3, loc2
            if loc1 > loc2:
                loc1, loc2 = loc2, loc1
            # 下面的三行代码将[loc1, loc2)区间的数据插入到loc3之后
            tmplist = solution_new[loc1:loc2].copy()
            solution_new[loc1:loc3 - loc2 + 1 + loc1] = solution_new[loc2:loc3 + 1].copy()
            solution_new[loc3 - loc2 + 1 + loc1:loc3 + 1] = tmplist.copy()
        value_new = 0
        for j in range(num - 1):
            value_new += distance[solution_new[j]][solution_new[j + 1]]
        value_new += distance[solution_new[0]][solution_new[51]]
        if value_new < value_current:  # 接受该解
            value_current = value_new
            solution_current = solution_new.copy()

            if value_new < value_best:
                value_best = value_new
                solution_best = solution_new.copy()
        else:  # 按一定的概率接受该解
            if np.random.rand() < np.exp(-(value_new - value_current) / t):
                value_current = value_new
                solution_current = solution_new.copy()
            else:
                solution_new = solution_current.copy()
    t = delta * t
    result.append(value_best)
print(solution_best)

