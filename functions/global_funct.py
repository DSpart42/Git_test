x = 50

def priX():
    global x
    print("Значение x равно: ", x)
    x = 15
    print("Заменили глобальное значение на: ", x)


priX()

print(x)
