import time

import pytest
from Project.BaseTest import BaseTest
from Project.Pages.Elements.SignUP.SignUP import StageLocators
from Project.Pages.Base.URL.SignUp.SignUp import URLS
from Project.DataBase.db_connection import Database
from Project.DataBase.queries.SignUp_queries.SignUp_quires import Queries


class TestRegister(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database()
        self.queries = Queries(self.db)

    def get_last_user_data(self):
        return self.queries.get_user_data()

    @pytest.mark.smoke
    def test_registration_welcome(self, driver):
        # Открываем URL
        driver.get(URLS.InstajetPTCatalog)

        # Создаем объекты StageLocators
        open_dialog_window = StageLocators(driver)
        field_email_input = StageLocators(driver)
        select_checkBox = StageLocators(driver)
        create_account = StageLocators(driver)

        # Проверяем, что объекты StageLocators не являются None
        assert open_dialog_window is not None, "Не удалось открыть диалоговое окно"
        assert field_email_input is not None, "Не удалось ввести сгенерированный Email в поле ввода"
        assert select_checkBox is not None, "Не удалось спроектировать выбранный чекбокс"
        assert create_account is not None, "Не удалось создать объект create_account"

        # Выполняем действия
        open_dialog_window.open_dialog_window()
        random_email = field_email_input.field_email_input()  # Здесь мы генерируем email и вводим его в поле ввода
        select_checkBox.select_checkBox()
        create_account.create_account()

        # Пауза, чтобы дождаться, когда токен появится в локальном хранилище
        time.sleep(15)

        # Извлекаем токен из локального хранилища до перезагрузки страницы
        user_token_from_cookie = driver.get_cookie('token')['value']

        # Выводим токен из локального хранилища на консоль
        print("Токен из куки:", user_token_from_cookie)

        # Получаем токен пользователя из базы данных
        last_user_data = self.get_last_user_data()
        user_id_from_database = last_user_data["id"]
        user_token_from_database = last_user_data["token"]

        # Формируем токен в формате id:token
        formatted_user_token_from_database = f"{user_id_from_database}:{user_token_from_database}"

        # Выводим сформированный токен из базы данных на консоль
        print("Сформированный токен из базы данных:", formatted_user_token_from_database)

        # Сверяем токены
        assert user_token_from_cookie == formatted_user_token_from_database, "Токены не совпадают"
