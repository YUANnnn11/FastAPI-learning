# 循环中断：continue，临时中断，跳过一次
for x in range(1,6):
    print("语句1")
    continue
    print("语句2")

print()

# continue的嵌套
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

print()
# 循环中断：break，跳出循环
for x in range(1,6):
    print("语句1")
    break
    print("语句2")

print()

# break的嵌套
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")