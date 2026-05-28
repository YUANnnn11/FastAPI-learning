class Phone:
    IMEI = 2024
    producer = "HM"

    def call_by_5g(self):
        print("开启5g通话")


# 定义一个类，对父类成员进行复写
class MyPhone(Phone):
    producer = "IT"             # 复写父类成员属性

    def call_by_5g(self):         # 复习父类成员方法
        print("以单核模式运行")
        # print("开启5g通话")

        # 在子类中调用父类成员
        # 方式1：
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2：
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()

        print("结束")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)