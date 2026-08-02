#   Python里面没有真正的私有,只是约定俗成私有前面加上_类目可以直接调用私有
class Car:
    def __init__(self, brand, model, color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner  #私有属性
    def start(self):
        print(f"{self.brand} {self.model} {self.color}正在启动")

    def run(self):
        print(f"{self.__owner}{self.brand}{self.model}正在行驶")
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand}{self.model}准备停车")

    def __control_fuel(self):
        print(f"{self.brand}正在控制油门")

    def get_owner(self):
        return self.__owner[0:1]+'**'
if __name__ == '__main__':
    car = Car(
        'Audi','A6','black','Joye')
    car.start()
    car.run()
    car.stop()
    print(car.get_owner())