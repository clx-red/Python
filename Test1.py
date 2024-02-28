# #'r'读，'r+' 从开头读写，'w'从开头写覆盖，'w+'从开头读写覆盖，'a'追加
# name = open(file='Test1.txt', mode='r',encoding='utf-8')
# lines = name.readlines()
# for line in lines:
#     print(line)
# name.close() #成员函数

# #第二种方法
# with open(file='Test1.txt', mode='w+',encoding='utf-8') as name2: 
#     name2.write('hello world!\n')
#     lines = name2.readlines()
# for line in lines:
#     print(line)


# #numpy学习
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])#创建数组
# arr2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])#二维
# print(arr)
# print(arr2.shape)#(2, 5)
# '''
# arr2([[1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5]])
# '''

# #形状操作
# arr3 = arr2.reshape(5, 2)#-1参数全排一行
# print(arr3.shape)#(5, 2)
# '''
# arr3([[1, 2],
#        [3, 4],
#        [5, 1],
#        [2, 3],
#        [4, 5]])
# '''

# arr4 = arr3.transpose()#转置
# '''
# arr4([[1, 3, 5, 2, 4],
#        [2, 4, 1, 3, 5]])
# '''

# print(type(arr))

# print(arr2[1][3])#二维索引

# print([1, 2, 3]+[4, 5, 6])#列表拼接

# #向量的加法，数组对应元素运算
# print(np.array([1, 2, 3])+np.array([4, 5, 6]))
# print(np.array([1, 2, 3])-np.array([4, 5, 6]))
# print(np.array([1, 2, 3])*np.array([4, 5, 6]))
# print(np.array([1, 2, 3])/np.array([4, 5, 6]))
# '''
# [1, 2, 3, 4, 5, 6]
# [5 7 9]
# [-3 -3 -3]
# [ 4 10 18]
# [0.25 0.4  0.5 ]
# '''

# #点乘
# arr_dot = np.dot(np.array([1, 2, 3]), np.array([4, 5, 6]))#32

# #数组平均值
# arr_avg = np.mean(arr4)#3

# #最大
# arr_max = np.max(arr4)#5

# #求和
# arr_sum = np.sum(arr4)#30

# #标准差
# arr_std = np.std(arr4)#1.4142135623730951

# #排序
# arr_sort = np.sort(arr4)
# '''
# arr_sort([[1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5]])
# '''

# #筛选
# arr_bool = arr4 > 3
# '''
# arr_bool([[False, False,  True, False,  True],
#        [False,  True, False, False,  True]])
# '''
# arr_st = arr4[arr_bool]
# '''
# arr_st([5, 4, 4, 5])
# '''

# arr_st1 = arr4[(arr4 > 2) & (arr4 < 5)]# &  按位 与 等效于在每一位上运行一次 and
#                                        # |  按位 或         ······          or
# '''
# arr_st1([3, 4, 4, 3])
# '''

# #保存和导入
# #以.npy存为二进制文件
# np.save("arr4",arr4)#保存

# print(np.load('arr4.npy'))#导入
# '''
# [[1 3 5 2 4]
#  [2 4 1 3 5]]
# '''