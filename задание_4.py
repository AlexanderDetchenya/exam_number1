m = int(input("Введите число m: "))
n = int(input("Введите число n(должно быть больше или равно m): "))
if m <= n:
    for i in range(m, n + 1):
        print(i)
else:
    print("Число n меньше числа m!")

