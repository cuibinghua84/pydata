# -*- coding: utf-8 -*-
"""
@author: 东风
@file: my_car.py
@time: 2019/11/4 14:11
"""

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()