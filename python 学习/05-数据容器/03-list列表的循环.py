# while 循环
def list_while_func():
    name_list = ["Tom", "Rose", "Lily"]
    index = 0
    while index < len(name_list):
        element = name_list[index]
        print(f"列表的元素有：{element}")
        index += 1



# for 循环
def list_for_func():
    age_list = [21, 25, 21, 23, 22, 20]
    for element in age_list:
        print(f"列表的元素有：{element}")




list_while_func()
list_for_func()


# 练习
def while_list(list):
    index = 0
    new_list = []
    while index < len(list):
        if list[index] % 2 == 0:
            new_list.append(list[index])
        index += 1
    return new_list

def for_list(list):
    new_list = []
    for element in list:
        if element % 2 == 0:
            new_list.append(element)
    return new_list

list = [1,2,3,4,5,6,7,8,9,10]
print(f"通过while循环，从列表：{list}中取出偶数，组成新列表：{while_list(list)}")
print(f"通过for循环，从列表：{list}中取出偶数，组成新列表：{for_list(list)}")

