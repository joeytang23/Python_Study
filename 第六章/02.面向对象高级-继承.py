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


class FuelCar(Car):
    pass

class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1 = FuelCar('BMW', model='X5', color='blue',owner='JOEY')
    c1.start()
    c1.stop()
    c1.run()
    print(c1.get_owner())
    print(c1.brand, c1.model, c1.color)
