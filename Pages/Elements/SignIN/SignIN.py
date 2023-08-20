from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project.Pages.Base.Methods import BasePage
from Project.Pages.Base.Utils.EmailGenerateor import Configuration
from Project.Pages.Base.Utils.credentials_generator import generate_random_credentials, random_string, generate_password


class LoginLocators(BasePage):
    EmailField = (By.XPATH, '//*[@id="__nuxt"]/div/div/main/div/div[1]/form/div[2]/div[1]')
    PasswordField = (By.XPATH, '//*[@id="__nuxt"]/div/div/main/div/div[1]/form/div[2]/div[2]')
    Auth = (By.XPATH, '//*[@id="__nuxt"]/div/div/main/div/div[1]/form/div[2]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email_and_password(self, email, password):
        """Ввод email и пароля."""
        self.enter_text(self.EmailField, email)
        self.enter_text(self.PasswordField, password)

    def generate_and_enter_random_credentials(self):
        """Генерация и ввод случайных учетных данных."""
        email, password = generate_random_credentials()
        self.enter_email_and_password(email, password)
        return email, password

    def click_auth(self):
        """Нажатие на кнопку авторизации."""
        self.click_element(self.Auth)

    @staticmethod
    def get_random_credentials_parameters():
        """Возвращает параметризованные случайные учетные данные."""
        return [
            generate_random_credentials(),
            generate_random_credentials()
        ]
