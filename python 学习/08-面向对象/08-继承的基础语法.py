# 单继承
class Phone:
    IMEI = 2024
    producer = "HM"

    def call_by_4g(self):
        print("4g开启")


class Phone2022(Phone):
    face_id = "001"

    def call_by_5g(self):
        print("2022新功能：5g开启")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "IT"

    def reader_card(self):
        print("读卡器")

    def writer_card(self):
        print("写卡器")

class RemoteControl:
    rc_type = "红外遥感"

    def control(self):
        print("红外遥感开启了")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass                    # 占位语句，为了完整性

phone2 = MyPhone()
phone2.call_by_4g()
phone2.reader_card()
phone2.writer_card()
phone2.control()

print(phone2.producer)      # 当继承的父类中有同名属性或方法，按顺序优先覆盖