# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def delete_dirs():
    try:
        for i in range(1, 10):
            name = os.path.join(os.getcwd(), 'dir_' + str(i))
            os.rmdir(name)
    except Exception as ex:
        print("Ошибка: " + str(ex))
        exit(-1)


if __name__ == '__main__':
    delete_dirs()
