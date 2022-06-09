s = input('Введите имя и фамилию через пробел: ')
s = s.split(' ')
s = s[::-1]
s = ' '.join(s)
print(s)



