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

    def charge(self):
        print(f"{self.brand}正在加能源")

    def get_owner(self):
        return self.__owner


class FuelCar(Car):
    def charge(self):
        print(f"{self.brand}正在加油")

class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand}正在充电")
#参数指定为父类类型,传入子类
def handle_charge(car :Car):
    car.charge()

if __name__ == '__main__':
    handle_charge(FuelCar('BMW', model='X5', color='blue',owner='zs'))
    handle_charge(ElectricCar('BYD', model='HAN', color='red',owner='LS'))