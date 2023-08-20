import time
import json
from urllib.parse import urlparse, parse_qsl, unquote

import pytest
from Project.BaseTest import BaseTest
from Project.Pages.Elements.SignUP.SignUP import StageLocators
from Project.Pages.Base.URL.SignUp.SignUp import URLS
from Project.DataBase.db_connection import Database
from Project.DataBase.queries.UTmQueries.UTmQueries import UtmQueries


class TestUTm(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database()
        self.queries = UtmQueries(self.db)

    def get_last_user_data(self):
        return self.queries.get_user_data()

    @pytest.mark.smoke
    def test_registration_welcome(self, driver):
        # Открываем URL
        driver.get(URLS.InstajetUTm)

        from urllib.parse import urlparse, parse_qs

        utm_local_storage = driver.execute_script("return window.localStorage.getItem('utm');")
        if utm_local_storage:
            print(f'Raw UTM from local storage: {utm_local_storage}')
            try:
                parsed_url = urlparse(utm_local_storage)
                utm_dict = dict(parse_qsl(parsed_url.query))  # Измененная строка
                print("Parsed UTM из локального хранилища:", utm_dict)
            except Exception as e:
                print("Ошибка при разборе UTM из URL:", e)
                utm_dict = None
        else:
            print("UTM не найден в локальном хранилище.")
            utm_dict = None

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

        # Ждем пока данные пользователя обновятся в базе данных
        time.sleep(5)

        # Получаем данные последнего зарегистрированного пользователя из базы данных
        user_data = self.get_last_user_data()

        # Проверяем, что данные пользователя были успешно получены
        assert user_data is not None, "Не удалось получить данные пользователя из базы данных"

        print("Email пользователя:", user_data['email'])

        # Раскодируем UTM метки в базе данных перед сравнением
        user_utm_dict = {k: unquote(v) for k, v in user_data['utm'].items()}

        # Печатаем UTM метку из базы данных
        print("UTM метка пользователя из базы данных:", user_utm_dict)

        # Проверяем, что UTM метка пользователя совпадает с той, что была в локальном хранилище
        assert utm_dict == user_utm_dict, "UTM метка из базы данных не совпадает с UTM меткой из локального хранилища"
