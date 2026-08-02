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
        return self.__owner

    def charge(self):
        print(f"{self.brand}{self.model}正在补充燃料..")


class FuelCar(Car):
    def charge(self):
        super().charge()
        Car.charge(self)
        print(f"{self.brand}{self.model}正在加油..")

class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand}{self.model}正在充电..")

if __name__ == '__main__':
    c1 = FuelCar('BMW','X5','BLACK','TYB')
    c1.charge()
