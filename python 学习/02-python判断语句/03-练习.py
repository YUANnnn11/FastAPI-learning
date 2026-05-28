import random
num = random.randint(1, 10)
guess_num = int(input("请输入你第一次猜测数字："))

if guess_num == num:
    print("恭喜你，猜对了")
else :
    if guess_num > num:
        print("你猜的数字太大了")
    else:
        print("你猜的数字太小了")

    guess_num = int(input("请输入你第二次猜测数字："))
    if guess_num == num:
        print("恭喜你，猜对了")
    else:
        if guess_num > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")

        guess_num = int(input("请输入你第三次猜测数字："))
        if guess_num == num:
            print("恭喜你，猜对了")
        else:
            print("三次机会，你都猜错了，我想的数字是%d" % num)