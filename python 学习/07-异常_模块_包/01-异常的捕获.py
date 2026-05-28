# 基本捕获异常的语法
try:
    f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt","r", encoding='UTF-8')
except:
    print("出现异常了,因为文件不存在，我们将用w模式去打开")
    # f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt", "w", encoding='UTF-8')


# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    print(name)
    print(1/0)
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除数为零的异常")

# 未正确设定异常类型，将无法捕获异常

#捕获所有异常
try:
    f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt","r", encoding='UTF-8')
except Exception as e:
    print("出现异常了")
    # f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt", "w", encoding='UTF-8')


# else: 没有异常时会执行
# finally：不管有没有异常都会执行
try:
    f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt","r", encoding='UTF-8')
except Exception as e:
    print("出现异常了")
    f = open("D:/pythonProject/python 学习/07-异常_模块_包/123.txt", "w", encoding='UTF-8')
else:
    print("太好了。没有异常了")
finally:
    print("结束")
    f.close()