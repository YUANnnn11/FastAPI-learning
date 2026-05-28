# for 变量 in 被处理的数据
name = "hello"
for x in name:
    print (x)


# 练习
name = "ithema is a brand of itcast"
count = 0
for i in name:
    if i == "a":
        count +=1
print(f"{name}中共含有：{count}个字母a")