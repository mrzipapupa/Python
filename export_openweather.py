import json
import csv
import os
import sys
import sqlite3


def print_help():
    print("help - получение справки")
    print('export_openweather.py --csv filename [<город>]')
    print('export_openweather.py --json filename [<город>]')


def connect_DB():
    name_db = 'weatherbase.db'
    cur_dir = os.getcwd()
    path_db = os.path.join(cur_dir, name_db)
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    try:
        city_param = sys.argv[3]
        query = "SELECT * FROM weather WHERE city = '{0}'".format(city_param)
        cursor.execute(query)
        if cursor.fetchone() is None:
            print("Не удается найти указанный город")
            raise IndexError
    except IndexError:
        cursor.execute("SELECT * FROM weather")
    return cursor


def export_csv(str_param):
    cursor = connect_DB()
    with open(str_param, 'w', newline='') as out_csv_file:
        csv_out = csv.writer(out_csv_file, delimiter=';')
        csv_out.writerow([d[0] for d in cursor.description])
        for result in cursor:
            csv_out.writerow(result)


def export_json(str_param):
    cursor = connect_DB()
    str_json = {}
    collection_json = []
    for str_res in cursor.fetchall():
        str_json['city_id'] = str_res[0]
        str_json['city'] = str_res[1]
        str_json['date'] = str_res[2]
        str_json['temperature'] = str_res[3]
        str_json['weather_id'] = str_res[4]
        collection_json.append(str_json.copy())
    with open(str_param, 'w') as out_json_file:
        json.dump(collection_json, out_json_file)


def get_str_params():
    do = {
        "help": print_help,
        "--csv": export_csv,
        "--json": export_json
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
            do[key](str_param)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")


if __name__ == '__main__':
    print('sys.argv = ', sys.argv)
    get_str_params()
