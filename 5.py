import math

def is_in_region_A_a(x, y):
    return x**2 + y**2 <= 4 and y >= x and x >= 0 and y >= 0


def is_in_region_A_b(x, y):
    return y <= 0.5 and y >= math.sin(x) and math.sin(x) >= 0.5


def is_in_region_V_a(x, y):
    return x**2 + y**2 <= 1 and y >= x


def is_in_region_V_b(x, y):
    return y >= x**2 and y <= 2 - x and y >= 0 and x >= 0 and x <= 2


# Пример проверки
print(is_in_region_V_b(1.0, 0.8))   # True (внутри треугольника)
print(is_in_region_V_b(1.5, 1.2))   # True
print(is_in_region_V_b(0.5, 1.5))   # False (выше y=2-x)
