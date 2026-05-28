# 定义字符串
str = "asdfghj"

# 通过下标索引取出字符串数据
element1 = str[2]
element2 = str[-5]
print(f"从字符串{str}中取出下标为2的的元素是{element1}，取出下标为-5的的元素是{element2}")

# 修改字符串数据
# str[0] = "A"       字符串不能修改

# index方法
str = "A and B"
index = str.index("and")
print(f"字符串{str}中and开始的下标位置是{index}")

# replace方法
str = "asdfghj"
new_str = str.replace("as","it")           # replace 后的字符串是创建了一个新的字符串
print(f"字符串{str}经过replace方法后的字符串是{new_str}")

# split方法
str = "A and B"
new_str_list = str.split(" ")
print(f"字符串{str}通过split方法以空格为分割后得到的字符串列表为{new_str_list}")

# strip方法
str = "   A and B   "
new_str = str.strip()       # 默认是删去前后空格
print(f"字符串{str}经过strip方法后的字符串是{new_str}")

str = "1222A 12and B22221"
new_str = str.strip("12")       # 前后含有指定任一字符的都删去
print(f"字符串{str}经过strip方法后的字符串是{new_str}")

# count方法
str = "1222A 12and B22221"
count = str.count("2")
print(f"字符串{str}中含有‘2’的数量是{count}")

# len函数
str = "1222A 12and B22221"
print(f"字符串{str}总元素是{len(str)}")


# while循环
index = 0
while index < len(str):
    print(str[index])
    index += 1


# for 循环
for x in str:
    print(x)



# 练习
str = "itheima itcast boxuegu"
count = str.count("it")
print(f"字符串{str}中有：{count}个it字符")

new_str = str.replace(" ","|")
print(f"字符串{str}，被替换空格后，结果：{new_str}")

new_str_list = new_str.split("|")
print(f"字符串{str}，按照|分隔后，得到：{new_str_list}")
