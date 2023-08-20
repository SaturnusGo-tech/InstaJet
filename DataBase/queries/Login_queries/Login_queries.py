import random
import string
import psycopg2.extras
from Project.DataBase.db_connection import Database


class LoginQueries:

    def __init__(self, db):
        self.db = db

    def get_user_referral_id(self):
        cursor = self.db.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT token FROM users ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        user_data = cursor.fetchone()
        return user_data

    def create_random_user(self):
        # Генерируем случайный имейл
        email = ''.join(random.choice(string.ascii_lowercase) for i in range(8)) + "@example.com"

        # Генерируем пароль
        password = ''.join(random.choice(string.digits) for i in range(8))  # 8 цифр
        password += random.choice(string.ascii_uppercase)  # одна заглавная буква
        password += random.choice(string.punctuation)  # один спец символ

        # Вставляем данные в базу данных
        cursor = self.db.conn.cursor()
        insert_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (email, password))
        self.db.conn.commit()

        # Выводим данные в терминале
        print(f"Email: {email}")
        print(f"Password: {password}")

        return email, password
