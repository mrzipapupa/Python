# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os


def is_dir(path):
    return os.path.exists(path) and not os.path.isfile(path)


def getdirs():
    dirs = os.listdir('.')
    for dir in dirs:
        if is_dir(dir):
            print(dir)


if __name__ == '__main__':
    getdirs()