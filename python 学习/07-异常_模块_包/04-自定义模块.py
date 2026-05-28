# 导入自定义模块使用
# import my_module1
# my_module1.test(1,5)
# from my_module1 import test
# test(1,6)


# 导入多个模块同名的功能，后者会覆盖前者
# from my_module1 import test
# from my_module2 import test
# test(2,5)


# __main__变量
# from my_module1 import test
# test(2,5)


# __all__变量
from my_module1 import *            # * 只能导入__all__列表里的功能（函数），除非手动导入模块内其他函数
test_a(1,4)
