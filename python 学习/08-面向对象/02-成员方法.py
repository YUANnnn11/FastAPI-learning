# 成员方法的定义与使用

class Student:
    name = None

    def say_hi1(self):
        print(f"大家好，我是{self.name}")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},我想对你说{msg}")



stu1 = Student()
stu1.name = "Lily"
stu1.say_hi1()

stu2 = Student()
stu2.name = "Rose"
stu2.say_hi2("hi")