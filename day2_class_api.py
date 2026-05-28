# ========== 任务 1：列表操作（第六章 01-06） ==========
# 写一个函数 process_scores(scores)
# scores 是一个数字列表，如 [85, 92, 78, 95, 88]
# 返回一个字典，包含以下统计：
#   - "最高分": 最大值
#   - "最低分": 最小值
#   - "平均分": 平均值（保留 1 位小数）
#   - "及格人数": 分数 >= 60 的人数
#   - "不及格名单": 分数 < 60 的分数组成的列表（按原顺序）
# 测试：process_scores([85, 92, 78, 95, 88])
#       process_scores([55, 42, 78, 60, 33])

def process_scores(scores):
    max_score = scores[0]
    min_score = scores[0]
    total = 0
    avg = 0.0
    count = 0
    fail_list = []

    for x in scores:
        if max_score <= x:
            max_score = x

        if min_score >= x:
            min_score = x

        total += x

        if x >= 60:
            count += 1
        else:
            fail_list.append(x)

    # avg = total / num
    avg = round(total/len(scores),1)              #   round()函数对数字四舍五入，round(数字, 保留几位小数)，不指定小数位，返回整数
    result = {
        "最高分": max_score,
        "最低分": min_score,
        "平均分":avg,
        "及格人数": count,
        "不及格名单": fail_list
    }

    return result

print(process_scores([85, 92, 78, 95, 88]))
print(process_scores([55, 42, 78, 60, 33]))






print()
# ========== 任务 2：字典操作（第六章 14-16） ==========
# 写一个函数 word_count(text)
# text 是一个英文句子，如 "hello world hello python world world"
# 统计每个单词出现的次数，返回字典 {"hello": 2, "world": 3, "python": 1}
# 提示：用 .split() 把句子拆成单词列表
# 测试：word_count("hello world hello python world world")


def word_count(text):
    word_list = text.split()
    word = set(word_list)

    result = {}
    while word:
        element =  word.pop()
        count = word_list.count(element)
        result[element] = count

    return result

print(word_count("hello world hello python world world"))


print()
# ========== 任务 3：列表 + 字典综合 ==========
# 写一个函数 filter_students(students, min_score)
# students 是字典列表：[{"name": "张三", "score": 85}, {"name": "李四", "score": 42}, ...]
# 返回分数 >= min_score 的学生名字列表，按分数从高到低排序
# 如果没有及格的学生，返回空列表 []
# 测试：filter_students([{"name": "张三", "score": 85}, {"name": "李四", "score": 42}, {"name": "王五", "score": 70}],60)

def filter_students(students,min_score):

    pass_list = []
    for x in students:
        if x["score"] >= min_score:
            pass_list.append(x)

    if len(pass_list) == 0:
        return []

    # sorted() 函数可以用 key 参数指定排序依据
    # reverse=True 表示降序（从高到低）
    sorted_list = sorted(pass_list,key = lambda student : student["score"],reverse=True)

    name_list = []
    for x in sorted_list:
        name_list.append(x["name"])

    return name_list

print(filter_students([{"name": "张三", "score": 85}, {"name": "李四", "score": 42}, {"name": "王五", "score": 70}],60))



print()
# ========== 任务 4：类与对象（第二阶段第一章 01-09） ==========
# 定义一个 Student 类
# - 属性：name(str), scores(list)
# - 方法：average() 返回平均分（保留 1 位小数）
# - 方法：best_subject() 返回最高分的下标（例：scores=[80,95,70] → 返回 1）
# - 方法：pass_or_fail() 平均分 >= 60 返回 True
# 创建 3 个 Student 实例，放入列表，遍历打印每人名字和是否及格

class Student:
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        count = 0
        for x in self.scores:
            total += x
            count += 1

        avg = round(total/count,1)
        return avg

    def best_subject(self):
        max_score = 0
        for x in self.scores:
            if x >= max_score:
                max_score = x
        return self.scores.index(max_score)

    def pass_or_fail(self):
        avg = self.average()
        if avg >= 60:
            return True
        else:
            return False

stu1 = Student("小王",scores=[80,95,70])
stu2 = Student("小妹",scores=[74,66,48])
stu3 = Student("小里",[12,88,45])

stu_list = [stu1,stu2,stu3]
for x in stu_list:
    print(f"姓名：{x.name},平均分是{x.average()},最好的成绩下标是：{x.best_subject()},是否合格{x.pass_or_fail()}")







print()
# ========== 任务 5：API 调用（需额外看 20min requests 教程） ==========
# pip install requests
# 用 requests.get() 调用 GitHub API：
#   https://api.github.com/users/你的GitHub用户名
# 打印返回 JSON 中的 login、name、public_repos 三个字段
# 用 try/except 包裹：请求失败时打印 "网络错误，请检查网络连接"

import requests
try:
    res = requests.get("https://api.github.com/users/YUANnnn11/")
except Exception as e:
    print(f"网络错误，请检查网络连接，错误原因是{e}")
else:
    data = res.json()
    print(data)
    print(data["login"])
    print(data["name"])
    print(data["public_repos"])
