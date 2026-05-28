# 字典的定义
my_dict = {"Tom": 95 ,"Lily": 88, "Rose":74}
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是{my_dict}，类型是{type(my_dict)}")
print(f"字典2的内容是{my_dict2}，类型是{type(my_dict2)}")
print(f"字典3的内容是{my_dict3}，类型是{type(my_dict3)}")


# 重复key的字典
my_dict = {"Tom": 95 ,"Tom": 88, "Rose":74}
print(f"重复key字典的内容是{my_dict}")


# 通过key取得value的值
my_dict = {"Tom": 95 ,"Tom": 88, "Rose":74}
score = my_dict["Tom"]
print(f"Tom的分数是{score}")
score2 = my_dict["Rose"]
print(f"Rose的分数是{score2}")

# 字典的嵌套
my_score_dict = {
    "Tom":{
        "语文":85,
        "数学":75,
        "英语":71
    },
    "Lily":{
        "语文":15,
        "数学":96,
        "英语":45
    },
    "Rose":{
        "语文":68,
        "数学":77,
        "英语":91
    }
}
print(f"嵌套字典的内容是{my_score_dict}")

# 取出嵌套字典里的数据
score = my_score_dict["Tom"]["英语"]
print(f"Tom的英语成绩是{score}")

score2 = my_score_dict["Lily"]["数学"]
print(f"Lily的数学成绩是{score2}")