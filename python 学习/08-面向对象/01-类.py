# 设计一个类（类比生活：设计一张登记表）
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建一个对象（打印一张表）
stu1 = Student()

# 对对象数据进行赋值（填表）
stu1.name = '小美'
stu1.gender = '女'
stu1.nationality = '中国'
stu1.native_place = '上海'
stu1.age = 18

# 获取对象中记录的属性信息
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)