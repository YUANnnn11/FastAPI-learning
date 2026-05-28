def query(show_header):
    if show_header:
        print("---------查询余额----------")
    print(f"{name}，您好，您账户的余额为{money}元")

def save(save_num):
    print("---------存款----------")
    global money
    money += save_num
    print(f"{name},您好，您存款{save_num}元成功")
    # print(f"{name},您好，您当前余额{money}")
    query(False)


def get(get_num):
    print("---------取款----------")
    global money
    money -= get_num
    print(f"{name},您好，您取款{get_num}元成功")
    # print(f"{name},您好，您当前余额{money}")
    query(False)


def main():
    print("---------主菜单----------")
    print(f"{name}，您好，欢迎来到ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3】")
    print("退出\t\t[输入4】")
    return int(input("请输入您的选择："))



money = 5000000
name = input("请输入您的姓名：")

while (True):
    num = main()
    if num == 1:
        query(True)
        continue
    elif num == 2:
        save_num = int(input("请输入你要存入的金额："))
        save(save_num)
        continue
    elif num == 3:
        get_num = int(input("请输入你要取出的金额："))
        get(get_num)
        continue
    else:
        print("退出")
        break