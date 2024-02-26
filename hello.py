# import sys
# from math import cos, radians
# # Create a string with spaces proportional to a cosine of x in degrees
# def make_dot_string(x):
#     return ' ' * int(20 * cos(radians(x)) + 20) + 'o'
# for i in range(360):
#     s = make_dot_string(i)
#     print(s)

# #乘法口诀表
# for a in range(10):
#     for b in range(a):
#         print("%dx%d= %2d" %(b+1,a,a*(b+1)),end='   ' )
#         if b+1 == a:
#             print()

# while True: 
#     a =int(input('Please input a integer:'))
#     if a == 0:
#         print('exit()')
#         break
#     elif a % 3 == 0:
#         print('%d is a multiple of 3' %(a))