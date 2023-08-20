from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project.Pages.Base.Methods import BasePage
from Project.Pages.Base.Utils.EmailGenerateor import Configuration


class StageLocators(BasePage):
    Open_dialog_window = (By.XPATH, '//*[@id="header"]/div/div/div[1]/a[1]')
    field_input_email = (By.XPATH, '//*[@id="modal-reg"]/div[2]/input')
    CheckBox = (By.XPATH, '//*[@id="modal-reg"]/label[1]/div[1]')
    click_on_created_account = (By.XPATH, '//*[@id="modal-reg"]/button[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_dialog_window(self, s=2):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(StageLocators.Open_dialog_window)
            )
        except TimeoutException:
            print("Timed out waiting for Open_dialog_window element to be clickable.")
            raise
        self.click_element(StageLocators.Open_dialog_window)
        self.sleep(s)

    def field_email_input(self, s=2):
        random_email = Configuration.generate_random_email()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(StageLocators.field_input_email)
            )
        except TimeoutException:
            print("Timed out waiting for element to be clickable.")
            raise

        element.clear()
        element.send_keys(random_email)
        self.sleep(s)

        return random_email

    def select_checkBox(self, s=2):
        self.click_element(StageLocators.CheckBox)
        self.sleep(s)

    def create_account(self, s=2):
        self.click_element(StageLocators.click_on_created_account)
        self.sleep(s)





