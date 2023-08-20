import random
import string


class Configuration:
    @staticmethod
    def generate_random_email():
        """Метод для генерации случайного email."""
        random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
        domain = "Saturn.com"  # Замените на ваш желаемый домен
        email = f"{random_string}@{domain}"
        return email


if __name__ == "__main__":
    from selenium import webdriver
