# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys

import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not str_param:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), str_param)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(str_param))
    except FileExistsError:
        print('директория {} уже существует'.format(str_param))


def copy_file():
    if not str_param:
        print("Необходимо указать имя файла вторым параметром")
        return
    copy_file_name = str_param + '.dupl'
    try:
        shutil.copy(str_param, copy_file_name)
        print('файл {} скопирован'.format(str_param))
    except FileExistsError:
        print('файл {} уже существует'.format(str_param))
    except FileNotFoundError:
        print('файла {} не существет'.format(str_param))


def delete_file():
    if not str_param:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.remove(str_param)
        print('файл {} удален'.format(str_param))
    except FileNotFoundError:
        print('файла {} не существет'.format(str_param))


def change_path():
    if not str_param:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        print('Директория до перехода: ', os.getcwd())
        os.chdir(str_param)
        print('Текущая директория: ', os.getcwd())
    except Exception as ex:
        print('Не найден указанный путь ', str_param, '. Подробнее: ', str(ex))


def view_full_path():
    try:
        print('Текущий путь: ', os.getcwd())
    except Exception as ex:
        print('Не удалось выполнить команду. Подробнее: ', str(ex))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "cd": change_path,
    "ls": view_full_path
}

try:
    str_param = sys.argv[2]
except IndexError:
    str_param = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
