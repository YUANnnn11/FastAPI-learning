# 使用构造方法对成员变量进行赋值


class Student:
    # name = None      构造方法下可以省略
    # age = None
    # gender = None

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Student类创建了一个对象")

stu = Student("小王",18,'男')
print(stu.name)
print(stu.age)
print(stu.gender)



class Info:
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr



for x in range(1,11):
    print(f"当前录入第{x}位学生信息，总共需要录入10位学生信息")
    stu = Info(input("请输入学生姓名："),input("请输入学生年龄："),input("请输入学生地址："))
    print(f"学生{x}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.addr}】")

