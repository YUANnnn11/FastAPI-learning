# if判断语句的基本语法
age = 18
if age >=18:
    print("我已经成年了")

print("程序结束")

age = 10
if age >= 18:
    print("我已经成年了")

print("程序结束")

#练习
print("欢迎来到儿童游乐园，儿童免费，成人需要补票10元")
age = int(input("请输入年龄："))
if age >= 18:
    print("你已成年，游玩需要补票10元")

print("祝你游玩愉快")

# if-else
print("欢迎来到儿童游乐园，儿童免费，成人需要补票10元")
age = int(input("请输入年龄："))
if age >= 18:
    print("你已成年，游玩需要补票10元")
else :
    print("你未成年，欢迎来到儿童游乐园")

print("祝你游玩愉快")

#练习
print("欢迎来到动物园")
height = int(input("请输入身高(cm)："))
if height > 120:
    print("你的身高超过120cm，游玩需要购票10元")
else:
    print("你的身高未超过120cm，可以免费游玩")

print("祝你游玩愉快")


# if-elif-else
print("欢迎来到动物园")
height = int(input("请输入身高(cm)："))
vip_level = int(input("请输入会员等级："))
day = int(input("请输入今天日期："))
if height < 120:
    print("你的身高未超过120cm，可以免费游玩")
elif vip_level > 3:
    print("你的会员等级高于3级，可以免费游玩")
elif day == 1:
    print("今天是1号，可以免费游玩")
else:
    print("你不符合免费条件，游玩需要购票10元")

print("祝你游玩愉快")

# 更简洁
if int(input("请输入身高(cm)：")) < 120:
    print("你的身高未超过120cm，可以免费游玩")
elif int(input("请输入会员等级：")) > 3:
    print("你的会员等级高于3级，可以免费游玩")
elif int(input("请输入今天日期：")) == 1:
    print("今天是1号，可以免费游玩")
else:
    print("你不符合免费条件，游玩需要购票10元")

print("祝你游玩愉快")

# 练习
print("猜猜我心里的数字")
num = 10
num_1 = int(input("请输入第一次猜想的数字："))
if num_1 != num:
    num_1 = int(input("不对，再猜一次："))
    if num_1 != num:
        num_1 = int(input("不对，再猜最后一次："))
        if num_1 != num:
            print("sorry,全猜错了，我想的数字是%d" % num)
        else:
            print("恭喜你，猜对了")
    else:
        print("恭喜你，猜对了")
else:
    print("恭喜你，猜对了")

# 练习 if和多elif
print("猜猜我心里的数字")
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你，猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你，猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜你，猜对了")
else:
    print("sorry,全猜错了，我想的数字是%d" % num)
