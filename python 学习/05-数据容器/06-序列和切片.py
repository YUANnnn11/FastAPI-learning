"""
 演示对不同序列进行切片操作
 语法： 序列[起始位置:结束位置(不含本身）:步长]
 起始位置:默认从头
 结束位置:默认到尾
 步长:默认为1
"""

# 对list进行切片，从1开始，4结束，步长为1
my_list = [0,1,2,3,4,5,6]
res1 = my_list[1:4]            # 步长默认为1可以不写
print(f"结果1是{res1}")

# 对tuple进行切片，从头开始，到最后结束，步长为1
my_tuple = (0,1,2,3,5,6)
res2 = my_tuple[:]            # 默认从头到尾，步长1，都可省略
print(f"结果2是{res2}")

# 对str进行切片，从头开始，到最后结束，步长为2
str = "0123456"
res3 = str[::2]
print(f"结果3是{res3}")

# 对str进行切片，从头开始，到最后结束，步长为-1
str = "0123456"
res4 = str [::-1]              # 即倒序输出
print(f"结果4是{res4}")

# 对列表进行切片，从3开始，1结束，步长为-1
my_list = [0,1,2,3,4,5,6]
res5 = my_list[3:1:-1]
print(f"结果5是{res5}")

# 对元组进行切片，从头开始，到尾结束，步长为-2
my_tuple = (0,1,2,3,5,6)
res6 = my_tuple[::-2]
print(f"结果6是{res6}")


# 练习
str = "万过月薪，员序程马黑来，nohtyp学"
# 方法一：倒序切片或切片倒序
step1 = str[::-1]
res1 = step1[9:14]
# 简化
res1 = str[::-1][9:14]
print(f"方法一的结果1：{res1}")

res2 = str[9:4:-1]
print(f"方法一的结果2：{res2}")

# 方法二：split分割“，”，replace替换“来”为空，倒序字符串
new_str = str.replace("来","")
new_str_list = new_str.split("，")
res3 = new_str_list[1][::-1]
# 简化
res3 = str.split("，")[1].replace("来","")[::-1]
print(f"方法二的结果：{res3}")