class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__ 魔术方法             实现类对象转字符串的行为（将对象信息从地址转换成字符串）
    def __str__(self):
        return f"Student类对象的名字是{self.name}，年龄是{self.age}"

    # __lt__ 魔术方法             比较两个类对象大于或小于
    def __lt__(self, other):
        return self.age < other.age


    # __le__ 魔术方法             比较两个类对象大于等于或小于等于
    def __le__(self, other):
        return self.age <= other.age



    # __eq__ 魔术方法              比较两个类对象相等
    def __eq__(self, other):
        return self.age == other.age


stu1 =Student("小美",18)
stu2 = Student("小王",20)
stu3 = Student("小李",20)
print(stu1)
print(str(stu1))

print(stu1 < stu2)
print(stu1 > stu2)

print(stu2 <= stu3)
print(stu2 >= stu3)

print(stu1 == stu2)
print(stu2 == stu3)

