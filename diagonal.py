"""
rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()  # 30.00
rectangle1.diagonal()  # 7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()  # 9.00
rectangle2.diagonal()  # 4.24
"""
import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.area = round(self.height * self.width, 3)
        self.diagonal = f'{math.sqrt(self.height ** 2 + self.width ** 2): .3}'


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area)
print(rectangle1.diagonal)

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area)
print(rectangle2.diagonal)
