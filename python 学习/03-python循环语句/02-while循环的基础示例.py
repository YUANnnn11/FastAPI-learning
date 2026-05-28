# 猜数字
import random
num = random.randint(1, 100)
flag = True
count = 0



while flag:
    guess_num = int(input("请输入你猜的数字:"))
    count += 1
    if guess_num == num :
        flag =False
        print ("恭喜你，猜对了")
    else :
        if guess_num > num :
            print("猜的数字大了")
        else :
            print("猜的数字小了")
print(f"你一共猜了{count}次")
