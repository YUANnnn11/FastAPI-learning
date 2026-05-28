def add(x,y):
    result = x + y
    print(f"{x} + {y} 的结果是 {result}")

add(4,8)


# 练习
def check(tepm):
    print("欢迎来到公司，请出示健康码，并配合测量体温！")
    if tepm <= 37.5:
        print(f"体温测量中，您的体温是：{tepm}度，体温正常请进")
    else:
        print(f"体温测量中，您的体温是：{tepm}度，需要隔离")


check(36.8)
check(38.2)