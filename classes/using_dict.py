ab = {
    'swaroop' : 'swaroop@gmail.com',
    'larry' : 'larry@lolchel.ru',
    'hanry' : 'hn@yahoo.net'
}

print('Адресс Swaroop\'a:', ab['swaroop'])

del ab['hanry']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакнт {0} с адресом {1}'.format(name,address))

ab['lolipop'] = 'sweets@hotmail.jp'

if 'lolipop' in ab:
    print('\nАдресс lolipop:', ab['lolipop'])