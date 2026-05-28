# 定义一个函数，接收另一个函数作为传入的参数
def test_func(compute):
    res = compute(2,8)
    print(f"compute参数的类型是{type(compute)}")
    print(f"计算结果是{res}")




# 定义一个函数，作为参数传入另一个函数
def compute(x,y):
    return x+y


# 调用，并传入函数参数
test_func(compute)