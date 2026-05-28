"""
    字典的常用操作
"""


# 新增元素
my_dict = {"Tom": 95 ,"Lily": 88, "Rose":74}
my_dict["Ken"] = 66
print(f"新增元素后的字典：{my_dict}")

# 更新元素
my_dict = {"Tom": 95 ,"Lily": 88, "Rose":74}
my_dict["Tom"] = 24
print(f"更新元素后的字典：{my_dict}")


# 删除元素
my_dict = {"Tom": 95 ,"Lily": 88, "Rose":74}
element = my_dict.pop("Lily")
print(f"删除元素后的字典：{my_dict}，删除的元素是：{element}")

# 清空字典
my_dict.clear()
print(f"清空元素后的字典：{my_dict}")


# keys获得所有key
my_dict = {"Tom": 95 ,"Lily": 88, "Rose":74}
keys = my_dict.keys()
print(f"获得字典全部的keys：{keys}")

# 遍历字典
# 方式1：用keys
for key in keys:
    print(f"字典的key：{key}")
    print(f"字典的值：{my_dict[key]}")

# 方式2：直接for遍历字典
for key in my_dict:
    print(f"字典的key：{key}")
    print(f"字典的值：{my_dict[key]}")



# 统计字典元素的数量
num = len(my_dict)
print(f"字典的元素数量是{num}")



# 练习
dict = {
    "wang":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "zhou":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "lin":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "zhang":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "liu":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"全体员工当前信息如下：\n{dict}")

for key in dict:
    if dict[key]["级别"] == 1:
        dict[key]["级别"] += 1
        dict[key]["工资"] += 1000

print(f"全体员工级别为1的员工完成升职加薪操作后信息如下：\n{dict}")