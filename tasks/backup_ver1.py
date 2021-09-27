import os
import time

soure = ['/Users/daniilbakin/Documents/MyDocuments']

target_dir = '/Users/daniilbakin/Documents/test'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

print(target)

zip_command = "zip -qp {0} {1}".format(target, ' '.join(soure))

print(zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось :(')
