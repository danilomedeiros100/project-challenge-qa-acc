import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebTablesPage:
    """Classe para interagir com a página Web Tables"""

    URL = "https://demoqa.com/webtables"

    # 📌 Seletores de elementos
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    TABLE_ROWS = (By.CLASS_NAME, "rt-tr-group")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    EDIT_BUTTON = (By.XPATH, "//span[@title='Edit']")

    # Campos do formulário
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Web Tables')]")  # Verifica se o título "Web Tables" está presente
    ADD_BUTTON = (By.ID, "addNewRecordButton")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Abre a página Web Tables"""
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PAGE_TITLE))

    def is_loaded(self):
        """Verifica se a página carregou corretamente verificando o botão de adicionar registro"""
        return bool(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ADD_BUTTON)))

    def open_add_record_modal(self):
        """Clica no botão ADD para abrir o formulário de novo registro e aguarda a abertura do modal"""
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_BUTTON))
        add_button.click()

        # Aguarda o modal aparecer completamente antes de tentar preenchê-lo
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        time.sleep(1)  # 🔹 Adiciona um pequeno delay para evitar `StaleElementException`

    def fill_registration_form(self, first_name, last_name, email, age, salary, department):
        """Preenche o formulário de registro"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(
            first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).send_keys(
            last_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.AGE_INPUT)).send_keys(age)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SALARY_INPUT)).send_keys(salary)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DEPARTMENT_INPUT)).send_keys(
            department)

    def submit_registration(self):
        """Clica no botão de envio do formulário"""
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_button.click()

        # Aguarda o modal ser fechado
        WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located(self.FIRST_NAME_INPUT))

    def is_record_present(self, record):
        """Verifica se um registro específico está presente na tabela"""
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows:
            if record["first_name"] in row.text and record["last_name"] in row.text:
                return True
        return False

    def is_table_empty(self):
        """Verifica se a tabela está vazia garantindo que a mensagem 'No rows found' esteja presente"""
        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: len(driver.find_elements(*self.TABLE_ROWS)) == 0 or self.is_no_data_message_present()
            )
            return True
        except:
            return False

    def delete_all_records(self):
        """Remove todos os registros da tabela de forma extremamente rápida."""

        # Sai imediatamente se a tabela já estiver vazia
        if self.is_no_data_message_present():
            return

        while True:
            delete_buttons = self.driver.find_elements(*self.DELETE_BUTTON)

            if not delete_buttons:
                break

            for button in delete_buttons:
                try:
                    self.driver.execute_script("arguments[0].click();", button)  # 🔹 Clique forçado via JavaScript

                    WebDriverWait(self.driver, 0.5).until(EC.staleness_of(button))

                    if self.is_no_data_message_present():
                        return
                except:
                    continue  # Continua mesmo se um clique falhar

    def edit_first_record(self, new_name):
        """Edita o primeiro registro da tabela alterando o nome"""
        self.driver.find_element(*self.EDIT_BUTTON).click()  # Clica no botão de edição
        first_name_field = self.driver.find_element(*self.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(new_name)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()  # Confirma a edição

    def update_first_name(self, new_name):
        """Altera o campo First Name no formulário de edição"""
        first_name_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))
        first_name_field.clear()
        first_name_field.send_keys(new_name)

    def delete_first_record(self):
        """Exclui o primeiro registro da tabela"""
        delete_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        delete_button.click()
        WebDriverWait(self.driver, 3).until(EC.staleness_of(delete_button))

    def click_add_button(self):
        """Clica no botão 'Add' para abrir o modal de registro"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def change_table_display_count(self, count=20):
        """Altera o número de registros exibidos na tabela."""
        select_element = self.driver.find_element(By.CSS_SELECTOR, "select[aria-label='rows per page']")
        select = Select(select_element)
        select.select_by_value(str(count))
        time.sleep(1)  # Pequeno delay para garantir que a tabela seja atualizada

        option_xpath = f"//option[@value='{count}']"
        option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, option_xpath))
        )

        # 🔹 Força o clique via JavaScript no elemento desejado
        self.driver.execute_script("arguments[0].click();", option)
        option_xpath = f"//option[@value='{count}']"
        option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, option_xpath))
        )

        # 🔹 Força o clique via JavaScript no elemento desejado
        self.driver.execute_script("arguments[0].click();", option)

    def is_no_data_message_present(self):
        """Verifica se a mensagem 'No rows found' está visível na tabela"""
        try:
            no_data_element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "rt-noData"))
            )
            return no_data_element.is_displayed()
        except:
            return False

    def is_modal_open(self):
        """Verifica se o modal de registro está aberto"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
            )
            return True
        except TimeoutException:
            return False