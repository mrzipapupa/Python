# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil


def copymain():
    filename = sys.argv[0]
    shutil.copy(filename, filename + '.copy')


if __name__ == '__main__':
    copymain()

