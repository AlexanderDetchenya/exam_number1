# import random
# N = 10
# a = [0] * N
#
# def fn(mn, mx):
#     for i in range(N):
#         a[i] = random.randint(mn, mx)
#
# mn = int(input(' '))
# mx = int(input(' '))
# fn(mn, mx)
# print(a)

# kort = (1, 2, 3, 4, 5, 6)
# kort1 = list(kort)
# kort2 = []
# for i in kort1:
#     if i != 3:
#         kort2.append(i)
# print(kort2)
# kort3 = tuple(kort2)
# print(type(kort3))

def summa(a, b):
    if all(type(x) in (int) for x in(a,b)):
        return a+b
    else:
        return f'{a}'+f'{b}'

print(summa(1, 3))
print(summa(1, 'b'))