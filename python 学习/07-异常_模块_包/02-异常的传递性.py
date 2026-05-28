# 定义一个有异常的方法
def func1():
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")

# 定义一个无异常的方法，调用上一个有异常的方法
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

# 定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(e)

main()
