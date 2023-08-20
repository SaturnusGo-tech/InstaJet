# database.py

import os
import psycopg2.extras
from dotenv import load_dotenv


class Database:

    def __init__(self):
        # Загружаем переменные из файла .env
        load_dotenv()

        # Читаем значения из переменных окружения
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        # Подключение к базе данных
        self.conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )

    def close(self):
        # Закрываем соединение с базой данных
        self.conn.close()

    def cursor(self):
        pass
