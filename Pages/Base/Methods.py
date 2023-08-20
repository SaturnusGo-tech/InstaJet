import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):

        element = self.driver.find_element(*locator)
        assert element, f"Элемент {locator} не найден"
        element.click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        assert element, f"Элемент {locator} не найден"
        element.send_keys(text)
        time.sleep(1)  # Добавляем задержку
        value_in_field = element.get_attribute("value")
        print(f"Значение в поле: {value_in_field}")  # Выводим значение из поля
        assert value_in_field == text, f"Введенный текст не соответствует значению поля ввода"
    def wait_for_element(self, locator, timeout=10):

        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            assert element, f"Элемент {locator} не найден"
        except TimeoutException:
            assert False, f"Элемент {locator} не появился за время {timeout} секунд"

    def sleep(self, seconds=5, randomize=False, min_seconds=None, max_seconds=None):
        if randomize:
            if min_seconds is None:
                min_seconds = 1
            if max_seconds is None:
                max_seconds = seconds * 2
            sleep_time = random.uniform(min_seconds, max_seconds)
        else:
            sleep_time = seconds
        time.sleep(sleep_time)
