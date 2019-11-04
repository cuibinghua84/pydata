# -*- coding: utf-8 -*-
"""
@author: 东风
@file: my_electric_car.py
@time: 2019/11/4 14:15
"""

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

