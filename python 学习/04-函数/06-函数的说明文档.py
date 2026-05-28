def add(x,y):
    """
    add函数可以接收两个参数，进行两数相加的功能
    :param x: 形参 x 表示相加的其中一个数字
    :param y: 表示相加的其中另一个数字
    :return: 返回值是两数相加的结果
    """
    result = x + y
    print(f"两数相加的结果是{result}")
    return result

res = add(5,7)
print (res)

add(4,5)