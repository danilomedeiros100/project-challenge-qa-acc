import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/browser-windows"

    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    PAGE_TEXT = (By.TAG_NAME, "body")  

    def open(self):
        """Abre a página de Browser Windows"""
        self.driver.get(self.url)

    def click_new_window_button(self):
        """Clica no botão de abrir nova janela"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.NEW_WINDOW_BUTTON)
        ).click()

    def is_new_window_opened(self):
        """Valida se a nova janela foi aberta e contém a mensagem esperada"""
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))  # Espera abrir a nova janela

        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        # Verifica se a mensagem esperada aparece
        page_text = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.PAGE_TEXT)
        ).text
        time.sleep(2)
        self.driver.close()  # Fecha a nova janela
        self.driver.switch_to.window(original_window)  # Volta para a principal

        return "This is a sample page" in page_text