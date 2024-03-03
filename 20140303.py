'''
################层次分析####################
总结：
层次分析法首先是要建立一个判断矩阵，判断矩阵为n*n型矩阵。
由于该矩阵的建立是通过一对一评价得出，所以要进行一致性检验。
规模越大一致性越差，只要是在可接受范围内即可。
计算最终权重的方法有：

1、算术平均法。各列各个元素/各列元素之和得到归一化矩阵，
再将归一化矩阵的各列元素求平均值得到权重。

2、几何平均法。将各行元素相乘得到的列向量各元素开n次方得到几何平均矩阵，
再将各值除以各值之和得到归一化矩阵，该矩阵即为权重。

3、特征值法。求出判断矩阵的特征值和特征向量，找到最大特征值所对应的特征向量，
将该向量归一化处理，即可得到权重。
'''
# #一致性检验
# import numpy as np
# A = np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
# #获取A的列数，1为行数
# n = A.shape[0]
# #求最大特征值和对应特征向量
# eig_val,eig_vec = np.linalg.eig(A)#eig_val 特征值，eig_vec特征向量
# #求最大特征值
# Max_eig = max(eig_val)
# #计算
# CI = (Max_eig - n) / (n - 1)
# RI = [0,0.0001,0.52,0.89,1.12,1.26,1.36,1.41,1.46,1.49,1.52,1.54,1.56,1.58,1.59]
# #RI最大支持n=15
# #避免n=2时一致矩阵分母为0，将其改为接近0的一个值
# CR = CI / RI[n-1]
# if CR <= 0.1:
#     print('Because CR <= 0.1, the consistency of matrix A is judged to be acceptable')
# else:
#     print('Because CR > 0.1, the consistency of matrix A is not acceptable')

# #算数平均法求权重
# #对N x M矩阵的列进行：每列各元素除各列之和的平均值
# import numpy as np
# A = np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
# #求每列的和
# Asumc = np.sum(A,axis=0)
# #获取A的列数
# n = A.shape[0]
# #归一化，二维数组除一维数组会自动将一维数组扩展成二维数组的形状，然后进行逐元素除法
# stand_A = A / Asumc
# #求每一行的和
# Asumr = np.sum(stand_A,axis=1)
# #计算权重向量
# weights = Asumr / n
# print('Arithmetic mean method weight vector is:\n',weights)

# #几何平均法求权重
# import numpy as np
# A = np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
# #每行各元素相乘
# prod_A = np.prod(A,axis=1)
# #计算列数
# n = A.shape[0]
# #将获得的向量各元素开n次方
# prod_n_A = np.power(prod_A,1/n)
# #归一化处理
# re_prod_A = prod_n_A / np.sum(prod_n_A)
# print('The weight vector of geometric mean method is:\n',re_prod_A)

# #特征值法求权重
# import numpy as np
# A = np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
# n = A.shape[0]
# eig_value,eig_vector = np.linalg.eig(A)
# #找最大特征值
# max_index = np.argmax(eig_value)#numpy中返回最大值下标的函数
# #max_index = list(eig_value).index(max(eig_value))#该方法寻找下标在list中可用需进行类型转换
# #找到最大特征值对应的特征向量
# max_vector = eig_vector[:,max_index]
# #对特征向量进行归一化处理得到权重
# weights = max_vector / np.sum(max_vector)
# print('The eigenvalue method finds the weight is:\n',weights)