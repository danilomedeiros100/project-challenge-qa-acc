from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    SUBJECTS = (By.ID, "subjectsInput")
    ADDRESS = (By.ID, "currentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGES = (By.CLASS_NAME, "error-message")
    SUCCESS_MODAL = (By.ID, "example-modal-sizes-title-lg")

    def open(self):
        self.driver.get(self.url)

    def is_page_loaded(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_form(self, first_name, last_name, email, mobile, subjects, address):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.MOBILE).send_keys(mobile)
        self.driver.find_element(*self.SUBJECTS).send_keys(subjects)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def is_success_modal_visible(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MODAL))

    def has_validation_errors(self):
        return len(self.driver.find_elements(*self.ERROR_MESSAGES)) > 0