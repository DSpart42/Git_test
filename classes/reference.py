print('простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

mylist = shoplist

del shoplist[0]

print('shoplist: ', shoplist)
print('mylist: ', mylist)

print('копирование путем полной вырезки')
mylist = shoplist[:]
shoplist.insert(0, 'яблоки')

print('shoplist: ', shoplist)
print('mylist: ', mylist)