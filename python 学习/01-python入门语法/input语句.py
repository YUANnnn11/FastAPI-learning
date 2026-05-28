print("告诉我你是谁")
name = input()
print("你叫%s"  %name)

name = input("请输入你的名字：")
print("你叫%s"  %name)

num = input("请输入数字：")
print("你输入的数字类型是：%s" %type(num))

num = int(num)
print("你输入的数字是：%d，类型是%s" %(num, type(num)))


# 练习
user_name = input("请输入用户名：")
user_type = input("请输入用户类型：")
print("用户名是：%s，用户类型是：%s" %(user_name, user_type))