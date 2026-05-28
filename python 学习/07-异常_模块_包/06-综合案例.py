import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("asdfghj"))
print(my_utils.str_util.substr("asdfghj",1,4))


file_util.append_to_file("D:/pythonProject/python 学习/07-异常_模块_包/123.txt","qwert")
file_util.print_file_info("D:/pythonProject/python 学习/07-异常_模块_包/123.txt")