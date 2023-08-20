import psycopg2.extras
from Project.DataBase.db_connection import Database


class Queries:

    def __init__(self, db):
        self.db = db

    def get_user_data(self):
        # Создаем курсор для выполнения SQL-запросов
        cursor = self.db.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Выполняем запрос для получения данных последнего созданного пользователя
        query = "SELECT id, token, email FROM users ORDER BY id DESC LIMIT 1"
        cursor.execute(query)

        # Получаем результат
        user_data = cursor.fetchone()

        return user_data

    def clear_user_data(self):
        # Создаем курсор для выполнения SQL-запросов
        cursor = self.db.conn.cursor()

        query = "DELETE FROM users WHERE email LIKE '%Saturn.com%'"
        cursor.execute(query)
