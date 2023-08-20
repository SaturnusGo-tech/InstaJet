
import random
import string


# Функция для генерации случайного email и пароля
def generate_random_credentials():
    email = f"{random_string(5)}@{random_string(3)}.com"
    password = generate_password()
    return email, password


# Вспомогательная функция для генерации случайной строки
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# Вспомогательная функция для генерации пароля
def generate_password():
    digits = ''.join(random.choice(string.digits) for _ in range(8))
    uppercase_letter = random.choice(string.ascii_uppercase)
    special_symbol = random.choice(string.punctuation)
    return digits + uppercase_letter + special_symbol
