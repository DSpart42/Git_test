shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('осталось сделать покупок: ', len(shoplist))

print('покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\n Так же нужно купить риса.')
shoplist.append('рис')
print('теперь мой список покупок таков:', shoplist)

print('отсортирую я свой список')
shoplist.sort()
print('отсортированный список выглядит так:', shoplist)

print('первое, что мне нужно купить, это:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('теперь мой список покупок:', shoplist)