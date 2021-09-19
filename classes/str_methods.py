name = 'swaroop'

if name.startswith('swa'):
    print('да имя начинается на "swa"')

if 'a' in name:
    print('да оно содержит строку "а"')

if name.find('war') != -1:
    print('да, оно содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия','Россия','Африка', 'Китай']

print(delimiter.join(mylist))
