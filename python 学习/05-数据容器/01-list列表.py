"""
    list列表语法：
    [元素1,元素2,元素3,...]
"""

# 定义一个list 列表
my_list = ["ajdl","awi","tyui","qwer"]
print(my_list)
print(type(my_list))

my_list = ["ajdl",666,13.14,True]
print(my_list)
print(type(my_list))


# 嵌套列表
my_list = [[1,2,3],"awi",666,[77,5,9]]
print(my_list)
print(type(my_list))


# 通过下标索引取出对应位置的数据
name_list = ["Tom","Rose","Lily"]
# 列表[下标索引]。从前往后取，下标从0开始，往后+1。从后往前取，下标从-1开始，往前-1
print(name_list[0])
print(name_list[1])
print(name_list[2])
# 错误：索引不能超出列表范围，否则会报错
# print(name_list[3])

# 通过下标索引取出数据（倒序取出）
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])


# 取出嵌套列表中的数据
my_list = [[1,2,3],"awi",666,[77,5,9]]
print(my_list[3][1])