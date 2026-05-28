# ========== 任务 1：字符串处理 + 条件判断 ==========
# 写一个函数 check_password(password)
# 规则：长度 >= 8 且包含数字 → 返回 "强密码"
#       长度 >= 8 但不含数字 → 返回 "中等密码"
#       长度 >= 6 且包含数字 → 返回 "中等密码"
#       长度 >= 6 但不含数字 → 返回 "中等密码"
#       长度 < 6 → 返回 "弱密码"
#       "abc12345" → 长度8含数字 → 强密码
#       "abcdefgh" → 长度8不含数字 → 中等密码
#       "abc1234"  → 长度7含数字 → 中等密码  ← 之前没定义的缺口
#       "abcdefg"  → 长度7不含数字 → 中等密码
#       "12345"    → 长度5含数字 → 弱密码
#       "abcde"    → 长度5不含数字 → 弱密码
# 测试：check_password("abc12345")、"abcde"、"abcdefg"、"12345"
def check_password(password):
    length = len(password)
    # count = 0
    has_digit = False
    for x in password:
        # 错误：if x == str(range(0,10)):
        #     count += 1
        if x in "0123456789":
            has_digit = True
            break

    if length >= 8:
        if has_digit:
            return "强密码"
        else:
            return "中等密码"
    elif length >= 6 :
            return "中等密码"
    else :
        return "弱密码"

result1 = check_password("abc12345")
print(f"abc12345是{result1}")

result2 = check_password("abcdefgh")
print(f"abcdefgh是{result2}")

result3 = check_password("abc1234")
print(f"abc1234是{result3}")

result4 = check_password("abcdefg")
print(f"abcdefg是{result4}")

result5 = check_password("12345")
print(f"12345是{result5}")

result6 = check_password("abcde")
print(f"abcde是{result6}")



# ========== 任务 2：循环 + 条件 ==========
# 写一个函数 fizz_buzz(n)
# 打印 1 到 n，但是：
#   能被 3 整除 → 打印 "Fizz"
#   能被 5 整除 → 打印 "Buzz"
#   能同时被 3 和 5 整除 → 打印 "FizzBuzz"
#   其他情况 → 打印数字本身
# 测试：fizz_buzz(20)
def fizz_buzz(n):
    for x in range(1,n+1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizz_buzz(20)




# ========== 任务 3：循环嵌套（for 里面套 for） ==========
# 写一个函数 print_triangle(height)
# 用 * 号打印一个直角三角形，高度为 height
# 例：print_triangle(4) →
# *
# **
# ***
# ****
def print_triangle(height):
    for i in range(1,height+1):
        for j in range(1,i+1):
            print("*",end='')
        print()

print_triangle(4)





# ========== 任务 4：函数综合（今天的重点） ==========
# 写一个函数 calc(operator, a, b)
# operator 是字符串："+" "-" "*" "/"
# 返回 a 和 b 的运算结果
# 如果 operator 不是以上四种，返回 "不支持的运算符"
# 如果是除法且 b==0，返回 "除数不能为0"
# 测试：calc("+", 3, 5)、calc("/", 10, 0)、calc("^", 1, 2)
def calc(operator,a,b):
    # if not operator in "+-*/":
    if operator not in ("+","-","*","/"):  # 可以改进成这句，但不改也没关系
        return "不支持的运算符"
    else:
        if operator == "/" and b == 0:
            return "除数不能为0"
        elif operator == "+":
            return a+b
        elif operator == "-":
            return a-b
        elif operator == "*":
            return a*b
        else:
            return a/b

res1 = calc("+", 3, 5)
print(res1)
res2 = calc("/", 10, 0)
print(res2)
res3 = calc("^", 1, 2)
print(res3)