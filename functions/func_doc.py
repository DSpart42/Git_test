def printMax(x, y):
    '''если это о чем я думаю, то это жесть'''

    # а это не должно выводится

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3,5)
print(printMax.__doc__)

print(max(10,max(1,20)))
