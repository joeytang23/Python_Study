#Python多态不依赖于继承关系,鸭子多态:像鸭子一样游泳就是鸭子,即关注方法
class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name} is swimming')

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def swimming(self):
        print(f'{self.age}岁的{self.name} is swimming')

class pig:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name} is swimming')

def go_swimming(duck:Duck):
    duck.swimming()

if __name__ == '__main__':
    duck = Duck('特洛伊',18)
    go_swimming(duck)
    go_swimming(Dog('旺财',18))

