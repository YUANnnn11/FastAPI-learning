# 数字类型转换为字符串
str1 = str(123)
print(type(str1), str1)

str2 = str(123.456)
print(type(str2), str2)

#字符串转换为数字
num_int = int("123")
print(type(num_int), num_int)

num_float = float("123.456")
print(type(num_float), num_float)

# 错误示范：尝试将字符串转化为数字时，字符串的内容必须是数字，否则会报错
# num = int("你好")
# print(type(num), num)

# 整数转换成浮点数
num1 = float(123)
print(type(num1), num1)

# 浮点数转换成整数
num2 = int(123.456)
print(type(num2), num2)