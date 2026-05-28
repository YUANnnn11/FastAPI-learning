# 定义集合：集合有去重功能，且集合是无序的
my_set = {"it","itproject","asdf","it","itproject","asdf","it","itproject","asdf"}
my_set_empty = set()
print(f"集合1的内容是{my_set}，类型是{type(my_set)}")
print(f"集合2的内容是{my_set_empty}，类型是{type(my_set_empty)}")

# 添加新元素
my_set = {"it","itproject","asdf"}
my_set.add("python")
my_set.add("it")
print(f"集合添加新元素后的内容是{my_set}")

# 移除元素
my_set = {"it","itproject","asdf"}
my_set.remove("asdf")
print(f"集合移除元素后的内容是{my_set}")

# 随机取出任一元素
my_set = {"it","itproject","asdf"}
element = my_set.pop()
print(f"集合取出的元素是{element}，集合的内容是{my_set}")

# 清空元素
my_set.clear()
print(f"集合清空元素后的内容是{my_set}")


# 取出两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出两个集合差集为{set3}，现集合1的内容为{set1}，现集合2的内容为{set2}")

# 消除两个元素的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"现集合1的内容为{set1}，现集合2的内容为{set2}")


# 合并两个集合为一个
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"取出两个集合差集为{set3}，现集合1的内容为{set1}，现集合2的内容为{set2}")


# 统计集合的元素
my_set = {"it","itproject","asdf","it","itproject","asdf","it","itproject","asdf"}
num = len(my_set)
print(f"集合里的元素数量是{num}")


# 集合的遍历
# 因为集合是无序的，无法用while循环遍历。用for循环
my_set = {"it","itproject","asdf"}
for element in my_set:
    print(element)


# 练习
my_list = ["黑马程序员","船只教育","黑马程序员","船只教育","itheima","itcast","itheima","itcast","best"]
my_set = set()
for x in my_list:
    my_set.add(x)
print(f"有列表：{my_list}\n存入集合后结果为：{my_set}")