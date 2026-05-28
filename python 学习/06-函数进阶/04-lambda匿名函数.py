def test_func(compute):
    res = compute(2,8)
    print(f"计算结果是{res}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test_func(lambda x,y:x+y)
test_func(lambda x,y:x*y)

# lambda函数用于临时构建一个函数，只用一次的场景。
# lambda函数不能换行写，只能写一行代码