# 语法1：range(num),0-num（不包含num本身）的数字序列
for x in range(5):
    print(x)
print()


#语法2：range(num1,num2),从num1-num2不包含num2本身）的数字序列
for x in range(5,10):
    print(x)
print()


#语法3：range(num1,num2,step),从num1-num2不包含num2本身）的间隔为step的数字序列
for x in range(5,10,2):
    print(x)
print()


# 练习：
num = 100
count = 0
for x in range(1,num):
    if x % 2 == 0:
        count += 1
print(f"1到{num}（不含{num}本身）范围内，有{count}个偶数")