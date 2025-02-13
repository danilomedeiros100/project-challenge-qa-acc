import os
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
    GENDER_MALE = (By.XPATH, "//label[contains(text(), 'Male')]")
    GENDER_FEMALE = (By.XPATH, "//label[contains(text(), 'Female')]")
    GENDER_OTHER = (By.XPATH, "//label[contains(text(), 'Other')]")
    MOBILE = (By.ID, "userNumber")
    SUBJECTS = (By.ID, "subjectsInput")
    ADDRESS = (By.ID, "currentAddress")
    FILE_UPLOAD = (By.ID, "uploadPicture")
    STATE_DROPDOWN = (By.ID, "state")
    CITY_DROPDOWN = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUCCESS_MODAL = (By.ID, "example-modal-sizes-title-lg")
    CLOSE_MODAL_BUTTON = (By.ID, "closeLargeModal")
    GENDER_RADIO_BUTTON = (By.CSS_SELECTOR, "input[name='gender']")

    def open(self):
        """Abre a página do formulário"""
        self.driver.get(self.url)

    def is_page_loaded(self):
        """Verifica se a página carregou corretamente"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )

    def fill_form(self, first_name, last_name, email, gender, mobile, subjects, address, state, city):
        """Preenche o formulário com os dados fornecidos"""
        self.fill_text_field(self.FIRST_NAME, first_name)
        self.fill_text_field(self.LAST_NAME, last_name)
        self.fill_text_field(self.EMAIL, email)
        self.select_gender(gender)
        self.fill_text_field(self.MOBILE, mobile)
        self.fill_subjects(subjects)
        self.fill_text_field(self.ADDRESS, address)
        self.select_dropdown(self.STATE_DROPDOWN, state)
        self.select_dropdown(self.CITY_DROPDOWN, city)

    def fill_text_field(self, locator, value):
        """Preenche um campo de texto"""
        field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)

    def select_gender(self, gender):
        """Seleciona o gênero com base na opção fornecida"""
        gender_locator = {
            "Male": self.GENDER_MALE,
            "Female": self.GENDER_FEMALE,
            "Other": self.GENDER_OTHER
        }.get(gender, self.GENDER_MALE)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(gender_locator)).click()

    def fill_subjects(self, subjects):
        """Preenche o campo de matérias"""
        subject_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.SUBJECTS))
        subject_input.send_keys(subjects)
        subject_input.send_keys(Keys.TAB)

    def select_dropdown(self, dropdown_locator, value):
        """Seleciona uma opção de um dropdown"""
        dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()

        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{value}')]"))
        )
        option.click()

    def upload_file(self, file_path):
        """Faz upload de um arquivo"""
        absolute_path = os.path.abspath(file_path)
        file_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.FILE_UPLOAD))
        file_input.send_keys(absolute_path)

    def submit_form(self):
        """Submete o formulário e aguarda a exibição do modal de sucesso"""

        # Garante que o botão de submissão está visível e clicável
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        # Faz scroll até o botão para garantir visibilidade
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        # Clica no botão de submit
        submit_button.click()

        # Aguarda até que o modal de sucesso seja visível
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL)
        )
    def submit_form_none(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()

    def get_highlighted_required_fields(self):
        """Retorna os campos obrigatórios que ficaram destacados como inválidos."""
        highlighted_fields = []
        required_field_selectors = [
            self.FIRST_NAME,
            self.LAST_NAME,
            self.MOBILE
        ]

        # Verifica se os campos de texto receberam um contorno vermelho
        for field in required_field_selectors:
            element = self.driver.find_element(*field)
            if not element.get_attribute("value"):  # Verifica se está vazio
                class_attr = element.get_attribute("class")
                if "is-invalid" in class_attr or "was-validated" in self.driver.find_element(By.ID,
                                                                                             "userForm").get_attribute(
                        "class"):
                    highlighted_fields.append(field)

        # Verificar separadamente os botões de rádio do gênero
        gender_radios = self.driver.find_elements(*self.GENDER_RADIO_BUTTON)
        if not any(radio.is_selected() for radio in gender_radios):  # Nenhum gênero foi selecionado
            highlighted_fields.append(self.GENDER_RADIO_BUTTON)

        return highlighted_fields




    def is_success_modal_visible(self):
        """Verifica se o modal de sucesso está visível"""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MODAL))

    def close_success_modal(self):
        """Fecha o modal de sucesso"""
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CLOSE_MODAL_BUTTON)).click()

    def fill_partial_form(self, **kwargs):
        """Preenche apenas os campos fornecidos, útil para testes negativos"""
        field_mapping = {
            "first_name": self.FIRST_NAME,
            "last_name": self.LAST_NAME,
            "email": self.EMAIL,
            "confirm_email": self.CONFIRM_EMAIL,  # Certifique-se que esse campo existe
            "password": self.PASSWORD,
            "mobile": self.MOBILE,
            "subjects": self.SUBJECTS,
            "address": self.ADDRESS,
            "state": self.STATE_DROPDOWN,
            "city": self.CITY_DROPDOWN
        }

        for key, locator in field_mapping.items():
            if key in kwargs and kwargs[key]:  # Somente preenche se o dado estiver presente
                self.fill_text_field(locator, kwargs[key])