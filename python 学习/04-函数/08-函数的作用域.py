# 局部变量
def test_a():
    num = 100
    print (num)

test_a()
# num在函数内定义，函数外无法使用
# print(num)



# 全局变量
num = 200
def test_b():
    print(num)

test_b()
print(num)



# 函数内修改全局变量
num = 300
def test_c():
    print (num)
def test_d():
    num = 500
    print(num)

test_c()
test_d()
print(num)

# 用global 关键词在函数内修改全局变量
num = 400
def test_e():
    print (num)
def test_f():
    global num # 设置内部定义的变量为全局变量
    num = 600
    print(num)

test_e()
test_f()
print(num)