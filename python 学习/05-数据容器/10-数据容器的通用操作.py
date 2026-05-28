my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcde"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}


# len函数
print(f"列表  个数是{len(my_list)}")
print(f"元组  个数是{len(my_tuple)}")
print(f"字符串 个数是{len(my_str)}")
print(f"集合  个数是{len(my_set)}")
print(f"字典  个数是{len(my_dict)}")

# max 函数
print(f"列表  最大的元素是{max(my_list)}")
print(f"元组  最大的元素是{max(my_tuple)}")
print(f"字符串 最大的元素是{max(my_str)}")
print(f"集合  最大的元素是{max(my_set)}")
print(f"字典  最大的元素是{max(my_dict)}")


# min 函数
print(f"列表  最小的元素是{min(my_list)}")
print(f"元组  最小的元素是{min(my_tuple)}")
print(f"字符串 最小的元素是{min(my_str)}")
print(f"集合  最小的元素是{min(my_set)}")
print(f"字典  最小的元素是{min(my_dict)}")


#类型转换：容器转换成列表
print(f"列表  转换成列表是{list(my_list)}")
print(f"元组  转换成列表是{list(my_tuple)}")
print(f"字符串 转换成列表是{list(my_str)}")
print(f"集合  转换成列表是{list(my_set)}")
print(f"字典  转换成列表是{list(my_dict)}")


#类型转换：容器转换成元组
print(f"列表  转换成元组是{tuple(my_list)}")
print(f"元组  转换成元组是{tuple(my_tuple)}")
print(f"字符串 转换成元组是{tuple(my_str)}")
print(f"集合  转换成元组是{tuple(my_set)}")
print(f"字典  转换成元组是{tuple(my_dict)}")


#类型转换：容器转换成字符串
print(f"列表  转换成字符串是{str(my_list)}")
print(f"元组  转换成字符串是{str(my_tuple)}")
print(f"字符串 转换成字符串是{str(my_str)}")
print(f"集合  转换成字符串是{str(my_set)}")
print(f"字典  转换成字符串是{str(my_dict)}")



#类型转换：容器转换成集合
print(f"列表  转换成集合是{set(my_list)}")
print(f"元组  转换成集合是{set(my_tuple)}")
print(f"字符串 转换成集合是{set(my_str)}")
print(f"集合  转换成集合是{set(my_set)}")
print(f"字典  转换成集合是{set(my_dict)}")


# sorted 排序
my_list = [3,1,5,4,2]
my_tuple = (3,1,5,4,2)
my_str = "caedb"
my_set = {3,1,5,4,2}
my_dict = {"key3":1,"key1":2,"key5":3,"key4":4,"key2":5}

print(f"列表  进行排序后是{sorted(my_list)}")
print(f"元组  进行排序后是{sorted(my_tuple)}")
print(f"字符串 进行排序后是{sorted(my_str)}")
print(f"集合  进行排序后是{sorted(my_set)}")
print(f"字典  进行排序后是{sorted(my_dict)}")

print(f"列表  进行反向排序后是{sorted(my_list,reverse=True)}")
print(f"元组  进行反向排序后是{sorted(my_tuple,reverse=True)}")
print(f"字符串 进行反向排序后是{sorted(my_str,reverse=True)}")
print(f"集合  进行反向排序后是{sorted(my_set,reverse=True)}")
print(f"字典  进行反向排序后是{sorted(my_dict,reverse=True)}")


