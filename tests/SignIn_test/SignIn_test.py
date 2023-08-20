import time
import pytest
from Project.BaseTest import BaseTest
from Project.Pages.Elements.SignIN.SignIN import LoginLocators
from Project.Pages.Base.URL.Login.LoginURLS import LoginUrl
from Project.DataBase.db_connection import Database
from Project.DataBase.queries.Login_queries.Login_queries import LoginQueries
from Project.Pages.Base.Utils.credentials_generator import generate_random_credentials


class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database()
        self.queries = LoginQueries(self.db)

    def get_last_user_data(self):
        return self.queries.get_user_referral_id()

    # Добавляем параметризацию
    @pytest.mark.parametrize("email,password", LoginLocators.get_random_credentials_parameters())
    @pytest.mark.smoke
    def test_login(self, driver, email, password):
        driver.get(LoginUrl.LoginPage)
        enter_email_and_password = LoginLocators(driver)
        enter_email_and_password.enter_email_and_password(email, password)
        click_auth = LoginLocators(driver)
        click_auth.click_auth()
