# 通过import 导入python自带的time模块使用sleep功能（函数）
# import time           # 导入Python内置的time模块（time.py）
# print("hello")
# time.sleep(5)         # 通过.就可以使用模块内部的全部功能（类、函数、变量）
# print("hi")

# 通过from 导入time模块的sleep功能（函数）
# from time import sleep
# print("hello")
# sleep(5)
# print("hi")



# 通过 * 导入time模块的全部功能
# from time import *
# print("hello")
# sleep(5)
# print("hi")


# 通过as 给特定功能加上别名
# import time as t
# print("hello")
# t.sleep(5)
# print("hi")

from time import sleep as sl
print("hello")
sl(5)
print("hi")