import math
def square(side_length):
    area = side_length ** 2
    return math.ceil(area)
side_length = int(input("Введите сторону квадрата: "))
print(square(side_length))