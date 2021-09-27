import os
import time

sourse = ['"/Users/daniilbakin/Documents/My Documents/Снимок экрана 2021-09-17 в 23.24.29.png"',
'"/Users/daniilbakin/Documents/My Documents/Снимок экрана 2021-09-17 в 23.27.03.png"',
'"/Users/daniilbakin/Documents/My Documents/Снимок экрана 2021-09-17 в 23.27.15.png"']

target_dir = '/Users/daniilbakin/Documents/test'

today = target_dir + os.sep + time.strftime('%Y.%m.%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qp {0} {1}'.format(target, ' '.join(sourse))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Все печально')