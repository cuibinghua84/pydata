# -*- coding: utf-8 -*-
"""
@author: 东风
@file: car.py
@time: 2019/11/4 11:14
"""


class Car():
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # 通过方法修改属性值
    def update_odometer(self, mileage):
        # 增加逻辑，禁止任何人将里程表读书往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")

    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 给子类定义属性和方法
        self.battery_size = 70
        self.battery = Battery()

    # 给子类定义属性和方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 重写父类的方法
    def fill_gas_tank(self):
        """电动车没有邮箱"""
        print("This car doesn't need a gas tank!")

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# # 直接修改属性值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 通过方法修改属性值
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# 通过方法对属性的值进行递增
# print("*" * 50)
# my_used_car = Car('subaru', 'outtack', 2016)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
