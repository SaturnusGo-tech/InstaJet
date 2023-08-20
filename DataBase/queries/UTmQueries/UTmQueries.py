import json
import psycopg2.extras
from Project.DataBase.db_connection import Database


class UtmQueries:

    def __init__(self, db):
        self.db = db

    def get_user_data(self):
        # Создаем курсор для выполнения SQL-запросов
        cursor = self.db.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Выполняем запрос для получения данных последнего созданного пользователя
        query = "SELECT email, utm FROM users ORDER BY id DESC LIMIT 1"
        cursor.execute(query)

        # Получаем результат
        user_data = cursor.fetchone()

        # Если пользователь найден и колонка 'utm' содержит словарь, используем его
        if user_data and 'utm' in user_data:
            user_data['utm'] = user_data['utm']  # здесь больше не нужно преобразование в JSON
        else:
            # Если 'utm' отсутствует или не содержит словарь, присвоим ему None
            user_data['utm'] = None

        return user_data

