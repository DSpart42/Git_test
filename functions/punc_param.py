def PrintMax(a,b):
    if a > b :
        print("Максимально: ", a)
    elif a == b :
        print(a, "Равно", b)
    else :
        print("Максимально: ", b)


s = int(input("введите s: "))
g = int(input("введите g: "))

PrintMax(s, g)