import math
a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
y = float(input('Введите число y: '))
y = 1/4*abs(math.sin(a+b+y)+math.sin(b+y-a)+math.sin(y+a-b)-math.sin(a+b+y))
print(y)