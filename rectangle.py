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

        self.area = f'{self.height * self.width: .2f}'
        self.diagonal = f'{math.sqrt(self.height ** 2 + self.width ** 2): .2f}'


rectangle1 = Rectangle(height=5, width=6)
print('高さ5､幅6の長方形の面積と対角線の長さ')
print(rectangle1.area)
print(rectangle1.diagonal)

rectangle2 = Rectangle(height=3, width=3)
print('高さ3､幅3の長方形(正方形)の面積と対角線の長さ')
print(rectangle2.area)
print(rectangle2.diagonal)
