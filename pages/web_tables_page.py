from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"

    # Locators
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    TABLE_ROWS = (By.XPATH, "//div[@class='rt-tr-group']")
    DELETE_BUTTONS = (By.XPATH, "//span[contains(@id, 'delete-record')]")

    def open(self):
        """Abre a página de Web Tables"""
        self.driver.get(self.url)

    def add_new_record(self, first_name, last_name, email, age, salary, department):
        """Adiciona um novo registro à tabela"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

        self.fill_text_field(self.FIRST_NAME, first_name)
        self.fill_text_field(self.LAST_NAME, last_name)
        self.fill_text_field(self.EMAIL, email)
        self.fill_text_field(self.AGE, age)
        self.fill_text_field(self.SALARY, salary)
        self.fill_text_field(self.DEPARTMENT, department)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def fill_text_field(self, locator, value):
        """Preenche um campo de texto"""
        field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        field.clear()
        field.send_keys(value)

    def count_table_rows(self):
        """Conta o número de linhas de dados na tabela, ignorando o placeholder 'No rows found'"""
        try:
            # Verifica se a mensagem "No rows found" está presente
            no_rows_element = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'No rows found')]")
            if no_rows_element:
                return 0  # Se a mensagem existir, a tabela está vazia

            # Caso contrário, conta as linhas normalmente
            rows = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-tr-group')]")
            return len(rows)
        except Exception as e:
            print(f"Erro ao contar linhas da tabela: {e}")
            return -1

    def delete_all_records(self):
        """Exclui todos os registros da tabela"""
        while True:
            try:
                delete_buttons = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".action-buttons span[title='Delete']"))
                )

                if not delete_buttons:
                    break  # Sai do loop se não houver mais registros

                for button in delete_buttons:
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView();", button)
                        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(button)).click()
                    except:
                        pass  # Ignora se um elemento específico não puder ser clicado

            except:
                break  # Sai do loop se os elementos não forem encontrados

    def set_page_size(self, size="25"):
        """Altera a quantidade de registros exibidos na tabela"""
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='rows per page']"))
        )
        dropdown.click()

        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{size}']"))
        )
        option.click()

    def close_ads_if_present(self):
        """Fecha anúncios que possam bloquear a interação"""
        try:
            iframe = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@id, 'google_ads_iframe')]"))
            )
            self.driver.switch_to.frame(iframe)
            close_button = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Fechar')]"))
            )
            close_button.click()
            self.driver.switch_to.default_content()
        except Exception:
            pass  # Se não houver anúncio, segue normalmente