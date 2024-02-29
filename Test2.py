# # 4x4 随机数组
# import numpy as np
# np.random.seed(1)#随机种子,每次随机数生成一致
# array = np.random.randint(0,100,16).reshape(4,4)
# '''
# array([[63, 61, 22, 57],
#        [ 1,  0, 60, 81],
#        [ 8, 88, 13, 47],
#        [72, 30, 71,  3]])
# '''
# print(array[array <= 10])#[9 5 1 6]
# print(np.sum(array[array <= 10]))#21


# #pandas 学习
# import pandas as pa
# df = pa.read_excel('鸢尾花数据集.xlsx','鸢尾花数据集',engine="openpyxl")
# date = {'id':[1,2,3,4],'name':['a','s','d','ff'],'number':[323,43,54,556]}#dictionary
# dfdate = pa.DataFrame(date)#制表
# '''
#     id	name	number
# 0	1	a	    323
# 1	2	s	    43
# 2	3	d	    54
# 3	4	ff	    56
# '''

# #基础信息
# print(df.head(5))
# print(df.info())

# #缺失值处理
# df_nan = df.dropna()
# print(df_nan)

# #数据类型转换
# df['PetalWidth']=df['PetalWidth'].astype(str)
# print(df.info())
# df['PetalWidth']=df['PetalWidth'].astype(float)
# print(df.info())

# #选择和过滤

# print(df[df["PetalWidth"] == 0.4])
# '''
#     SepalLength  SepalWidth  PetalLength  PetalWidth         Class
# 4           5.4         3.9          1.7         0.4   Iris-setosa
# 12          5.7         4.4          1.5         0.4   Iris-setosa
# 13          5.4         3.9          1.3         0.4   Iris-setosa
# 18          5.1         3.7          1.5         0.4   Iris-setosa
# 23          5.0         3.4          1.6         0.4   Iris-setosa
# 28          5.4         3.4          1.5         0.4   Iris-setosa
# 39          5.1         3.8          1.9         0.4   Iris-setosa
# '''

# lb = df['SepalLength'].mean() -  df['SepalLength'].std()#上界
# ub = df['SepalLength'].mean() + 3 * df['SepalLength'].std()#下界
# df[(df["SepalLength"] >= lb) & (df["SepalLength"] <= ub)].info()