"""
 封装中私有成员的使用
 私有成员以__开始定义：__name
"""

# 定义一个类，含有私有成员变量和私有成员方法
class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("以单核运行")

    def self_use(self):
        if self.__current_voltage >= 1:
            print("手机电压充足")
        else:
            self.__keep_single_core()
            print("手机电压不足，将以单核运行")




phone = Phone()
# print(phone.__current_voltage)
# phone.__keep_single_core()
phone.self_use()
