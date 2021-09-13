def maximum(x, y): #есть уже готовая функция (max)
    if x > y:
        return x
    elif x == y:
        return 'числа равны'
    else:
        return y

x = int(input('x = '))
y = int(input('y = '))

print(maximum(x, y))
