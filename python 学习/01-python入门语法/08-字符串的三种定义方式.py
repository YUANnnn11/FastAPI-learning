# 单引号定义法
name = '张三'
print(name)
print(type(name))

# 双引号定义法
name = "张三"
print(name)
print(type(name))

# 三引号定义法，跟注释的写法一样
name = """
我是
张三
"""
print(name)
print(type(name))


# 若要输出单引号
name = "'张三'"
print(name)

# 若要输出双引号
name = '"张三"'
print(name)

# 使用转义字符，解除引号效果
name = "\"张三\""
print(name)
name = "\'张三\'"
print(name)
