# python中print 会自动换行，要想不自动换行可以这样写
print("hello ")
print("world")
print("hello ",end='')
print("world")

# 通过\t对齐
print("hello\tworld")
print("very\tgood")

# 99乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t",end='')
        # if j == i:
        #     print()
        j += 1
    i += 1
    print()