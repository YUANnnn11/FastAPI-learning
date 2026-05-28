# 定义一个元组
t1 = ("asdf","ad","qa")
t2 = ()               # 空元组
t3 = tuple()          # 空元组

print(f"t1元组的类型是{type(t1)}，内容是{t1}")
print(f"t2元组的类型是{type(t2)}，内容是{t2}")
print(f"t3元组的类型是{type(t3)}，内容是{t3}")

# 定义单个元素的元组：末尾要加上逗号，否则不是元组类型而是str
t4 = ("hello",)
print(f"t4元组的类型是{type(t4)}，内容是{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5元组的类型是{type(t5)}，内容是{t5}")

# 下标索引取出内容
num = t5[1][2]
print(f"从t5元组取出的元素是{num}")


# 元组操作：index查找
index = t1.index("qa")
print(f"t1元组中的qa元素下标索引是{index}")

# 元组操作：count统计
t6 = ("asdf","ad","qa","ad","ad","ad","ad")
count = t6.count("ad")
print(f"t6元组中ad的数量是{count}")

# 元组操作：len函数统计元组元素总数
print(f"t6元组中元素的总个数是{len(t6)}")

# while循环
index = 0
while index < len(t1):
    print(f"元组中的元素有：{t1[index]}")
    index +=1

# for循环
for element in t1:
    print(f"t1元组中的元素有：{element}")


# 修改元组中元素
# t1[0] = "qqq"
# 元组中的元素不能被修改，会报错

# 但元组中嵌套的列表元素能被修改
t7 = ("adf","ioo",[1,2,3])
t7[2][0] = 55
print(f"t7元组的内容是{t7}")


# 练习
t8 = ('周杰伦',11,['football','music'])
index = t8.index(11)
name = t8[0]
print(f"年龄的下标位置为{index}，学生的姓名是{name}")
del t8[2][0]
t8[2].append('coding')
print(f"元组内容:{t8}")