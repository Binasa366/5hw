def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    summa = 1 + sum(a, b - 1)
    return summa


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(sum(a, b))