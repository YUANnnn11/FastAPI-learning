my_list = ["it","python","asdf"]

# 1.1查找元素的下标索引
index = my_list.index("python")
print(f"python在列表中的索引是{index}")

#1.2 当查找的元素在列表中不存在时，会报错
# index = my_list.index("hello")
# print(f"python在列表中的索引是{index}")

# 2.修改列表中某一元素
my_list[0] = "hello"
print(f"修改元素后，列表结果为{my_list}")

# 3.在列表中插入元素
my_list.insert(1,"qwer")
print(f"插入元素后，列表结果为{my_list}")

# 4.在列表末尾追加‘单个’元素
my_list.append("abc")
print(f"追加元素后，列表结果为{my_list}")

# 5.在列表末尾追加‘一批’元素
add_list = [1,2,3]
my_list.extend(add_list)
print(f"追加一批元素后，列表结果为{my_list}")

# 6.删除元素（2种方法）
    # 6.1 del
del my_list[0]
print(f"删除元素后，列表结果为{my_list}")

    # 6.2 pop
element = my_list.pop(1)
print(f"删除元素后，列表结果为{my_list},删除的元素为{element}")

# 7.清空列表
name_list = ["Tom","Rose","Lily"]
name_list.clear()
print(f"清空元素后，列表结果为{name_list}")

# 8.删除列表中指定的第一次出现的某一个元素(删除第一个匹配项）
name_list = ["Tom","Rose","Tom","Rose","Lily"]
name_list.remove("Rose")
print(f"删除第一次出现的Rose元素后，列表结果为{name_list}")

# 9.统计某元素在列表中出现的次数
name_list = ["Tom","Rose","Tom","Rose","Lily","Rose"]
count = name_list.count("Rose")
print(f"列表中Rose元素一共出现了{count}次")


#10.统计列表长度
name_list = ["Tom","Rose","Tom","Rose","Lily","Rose"]
count = len(name_list)
print(f"列表中共有{count}个元素")



# 练习
age_list = [21,25,21,23,22,20]

age_list.append(31)
print(f"现在列表结果为{age_list}")
new_list = [29,33,30]
age_list.extend(new_list)
print(f"现在列表结果为{age_list}")
# element1 = age_list.pop(0)
element1 = age_list[0]
print(f"现在列表结果为{age_list},取出的元素为{element1}")
# element2 = age_list.pop(len(age_list)-1)
element2 = age_list[-1]
print(f"现在列表结果为{age_list},取出的元素为{element2}")
index = age_list.index(31)
print(f"元素31的下标为{index}")

