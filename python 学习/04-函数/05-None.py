# 无return语句的函数返回值
def say_hi1():
    print("hello")

result = say_hi1()
print(f"无返回值函数，返回的内容是{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

# 主动返回None的函数
def say_hi2():
    print("hello")
    return None

result = say_hi2()
print(f"无返回值函数，返回的内容是{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

# None用于if判断
def age_check(num):
    if num > 18:
        return "SUCCESS"
    else:
        return None

result = age_check(10)
if not result:
    print("未成年,不让进")


# None 用于声明无初始内容的变量
name = None