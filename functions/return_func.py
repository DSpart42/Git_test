def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'числа равны'
    else:
        return y

x = int(input('x = '))
y = int(input('y = '))

print(maximum(x, y))
