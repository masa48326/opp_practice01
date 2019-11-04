"""
# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  #3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85

"""
import math

class Circle:
    def __init__(self, radius):
        self.area = (radius ** 2) * math.pi
        self.perimeter = radius * 2 * math.pi


circle1 = Circle(radius=1)
print('半径1の円の面積と円周の長さ')
print(f'{circle1.area: .2f}')
print(f'{circle1.perimeter: .2f}')

circle3 = Circle(radius=3)
print('半径3の円の面積と円周の長さ')
print(f'{circle3.area: .2f}')
print(f'{circle3.perimeter: .2f}')
