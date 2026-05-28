# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(1000,2000)


# 创建2个闹钟对象并让其工作
clo1 = Clock()
clo1.id = "001"
clo1.price = 19.9
print(f"闹钟的id是{clo1.id}，价格是{clo1.price}")
clo1.ring()

clo2 = Clock()
clo2.id = "002"
clo2.price = 10.5
print(f"闹钟的id是{clo2.id}，价格是{clo2.price}")
clo2.ring()