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


    def stop(self):
        print(f"{self.brand}{self.model}准备停车")


    def get_owner(self):
        return self.__owner

    def charge(self):
        print(f"{self.brand}{self.model}正在补充燃料..")

class HuaweiAiDriving:
    def __init__(self, version='v1'):
        self.version = version

    def run(self):
        print(f"使用华为AI智能驾驶系统{self.version}正在行驶....")

class WenJieCar(Car, HuaweiAiDriving):
    def __init__(self, brand,model,color,owner,version='v1'):
        Car.__init__(self,brand,model,color,owner)
        HuaweiAiDriving.__init__(self,version)
    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)

#MRO: Method Resolution Order 方法解析顺序,优先自己,然后是继承顺序
if __name__ == '__main__':
    car = WenJieCar('BMW','X5','黑色','张三')
    print(car.__dict__)
    car.run()