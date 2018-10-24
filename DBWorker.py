import os
import sqlite3


class DbWorker:
    def __init__(self):
        name_db = 'weatherbase.db'
        self.cur_dir = os.getcwd()
        self.path_db = os.path.join(self.cur_dir, name_db)
        self.conn = sqlite3.connect(self.path_db)
        if not os.path.exists(self.path_db):
            try:
                cursor = self.conn.cursor()
                cursor.execute("CREATE TABLE 'weather' ('city_id' INTEGER PRIMARY KEY, 'city' VARCHAR(255), "
                               "'date' DATE, 'temperature' INTEGER,'weather_id' INTEGER);")
                self.conn.commit()
            except sqlite3.Error as e:
                print('Ошибка БД: ' + str(e))

    def append_to_table(self, weather_collection):
        try:
            cursor = self.conn.cursor()
            query = "INSERT OR REPLACE INTO weather(city_id, city, date, temperature, weather_id) " \
                    "VALUES (:id, :city, :date, :temperature, :weather_id);"
            cursor.execute(query, weather_collection)
            self.conn.commit()

        except sqlite3.Error as e:
            print('Ошибка БД: ' + str(e))

    def print_results(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM weather')
        for r in cursor.fetchall():
            print(r)

    def clear_results(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM weather')
        self.conn.commit()

    def erase(self):
        cursor = self.conn.cursor()
        cursor.execute('DROP TABLE weather')
        self.conn.commit()

    def commit(self):
        self.conn.commit()
