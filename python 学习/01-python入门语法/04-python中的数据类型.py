# 方式一：用print语句直接输出类型信息
print(type(666))
print(type("哈哈哈哈哈"))
print(type(13.14))

# 方式二：使用变量存储type()语句的结果
int_type = type(666)
string_type = type("哈哈哈哈哈")
float_type = type(13.14)
print(int_type)
print(string_type)
print(float_type)

# 方式三：用type()查看变量存储的数据类型
name = "小王"
str_type = type(name)
print(str_type)