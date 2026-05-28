
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")

def make_noise(animal:Animal):
    animal.speak()

# 多态，使用两个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 演示抽象类
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美德空调制冷")

    def hot_wind(self):
        print("美德空调制热")

    def swing_l_r(self):
        print("美德空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)