from multiprocessing.connection import address_type


def info_func(name,age,gender):
    print(f"姓名：{name},年龄：{age}，性别：{gender}")


# 位置参数 （默认使用）
info_func('小王',20,'男')

# 关键字参数
info_func(name='小妹',age=18,gender='女')
info_func(age = 27,name='小李',gender='男')       # 可以不按顺序
info_func('小王',age=18,gender='男')              # 可以与位置参数混用



# 缺省参数（默认值）：默认值参数必须定义在最后
def info_func_1(name,age,gender='男'):
    print(f"姓名：{name},年龄：{age}，性别：{gender}")

info_func_1('小王',20)
info_func_1(name='小妹',age=18,gender='女')


# 不定长参数（可变参数）
# 位置不定长（*args）
def user_info(*args):
    print(f"args参数的类型是{type(args)}，内容是{args}")

user_info(1,2,3,"tee")


# 关键字不定长（**kwargs）   key - word
def user_info(**kwargs):
    print(f"kwargs参数的类型是{type(kwargs)}，内容是{kwargs}")

user_info(name = '小王',age=12,gender ='男',addr ='上海')