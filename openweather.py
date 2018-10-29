import datetime

import requests
from DBWorker import DbWorker
import json


def find_cities(cities, country):
    for city in cities:
        if city['country'] == country:
            yield city


def get_weather(id_city, app_id):
    http_req = "http://api.openweathermap.org/data/2.5/weather?id={0}&units=metric&appid={1}".format(id_city, app_id)
    return requests.get(http_req, proxies={"http": "http://94.242.57.136:10010"}).json()


def add_to_db(city):
    weather_json = get_weather(str(city['id']), app_id)
    db_coll = {'id': city['id'], 'city': city['name'], 'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
               'temperature': weather_json['main']['temp'], 'weather_id': weather_json['weather'][0]['id']}
    db.append_to_table(db_coll)


if __name__ == '__main__':
    with open('app.id', 'r') as file_id:
        app_id = file_id.readline()
    db = DbWorker()
    # db.clear_results()
    # db.erase()

    with open('city.list.json', 'r', encoding='utf-8') as cities_file:
        cities_list = json.load(cities_file)

    user_answer = input("Введите название города или аббревиатуру старны для поиска:")
    if len(user_answer) == 2:
        for city in find_cities(cities_list, user_answer.upper()):
            add_to_db(city)
    else:
        for city in cities_list:
            if city['name'] == user_answer:
                add_to_db(city)
    # db.commit()
    db.print_results()
