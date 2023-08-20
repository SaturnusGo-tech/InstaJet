import time

import pytest
from Project.BaseTest import BaseTest
from Project.Pages.Elements.SignUP.Referal_SignUp.Referal_SignUP import StageLocators
from Project.Pages.Base.URL.SignUp.SignUp import URLS
from Project.DataBase.db_connection import Database
from Project.DataBase.queries.Refferal_queries.Refferal_queires import Queries


class TestReferralCode(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database()
        self.queries = Queries(self.db)

    def get_last_user_data(self):
        return self.queries.get_user_referral_id()

    @pytest.mark.smoke
    def test_referral_code(self, driver):
        driver.get(URLS.InstajetReferral)

        time.sleep(20)

        # Получаем referral_code из локального хранилища
        referral_code = driver.execute_script("return window.localStorage.getItem('refferal_code');")

        # Проверяем, что referral_code был корректно сохранен в localStorage
        assert referral_code is not None, "Referral code не был сохранен в локальном хранилище"

        # Выводим refferal_code из локального хранилища на консоль
        print("Referral code из локального хранилища:", referral_code)

        # Создаем объекты StageLocators
        open_dialog_window = StageLocators(driver)
        field_email_input = StageLocators(driver)

        create_account = StageLocators(driver)

        # Выполняем действия
        open_dialog_window.open_dialog_window()
        random_email = field_email_input.field_email_input()  # Здесь мы генерируем email и вводим его в поле ввода

        create_account.create_account()

        user_data = self.get_user_referral_id()

        # Извлекаем реферальный код из базы данных
        referral_code_from_database = user_data["referral_id"]

        # Проверяем, что referral_id был корректно сохранен в базе данных
        assert referral_code_from_database is not None, "Referral code не был сохранен в базе данных"

        # Выводим реферальный код на консоль
        print("Реферальный код из базы данных:", referral_code_from_database)

        # Проверяем, что реферальный код из базы данных совпадает с реферальным кодом из localStorage
        assert referral_code == referral_code_from_database, "Реферальный код из базы данных не совпадает с реферальным кодом из localStorage"
