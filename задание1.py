# 1.	Используя стандартные арифметические операции представьте самое большое
# целое число из цифр 4, 4, 4 и приведите его значение.
perv = int(input('Введите первое число: '))
vtor = int(input('Введите второе число: '))
tret = int(input('Введите третье число: '))
if perv > vtor > tret:
    print("Naibolshee chislo", perv)
elif perv > tret > vtor:
    print("Naibolshee chislo", perv)
elif vtor > perv > tret:
    print("Naibolshee chislo", vtor)
elif vtor > tret > perv:
    print("Naibolshee chislo", vtor)
elif tret > vtor > perv:
    print("Naibolshee chislo", tret)
elif tret > perv > vtor:
    print("Naibolshee chislo", tret)
elif tret >= perv > vtor:
    print("Первое и третье число равны между собой и имеют максимальное значение: ", perv)
elif tret >= vtor > perv:
    print("Второе и третье число равны между собой и имеют максимальное значение: ", tret)
elif perv >= vtor > tret:
    print("Первое и второе число равны между собой и имеют максимальное значение: ", perv)
else:
    print("Все числа равны между собой и их значение: ", perv)
