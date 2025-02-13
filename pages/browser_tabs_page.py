from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserTabsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/browser-windows"

    NEW_TAB_BUTTON = (By.ID, "tabButton")
    PAGE_TEXT = (By.TAG_NAME, "body")  # O texto esperado aparece no body

    def open(self):
        """Abre a página de Browser Windows"""
        self.driver.get(self.url)

    def click_new_tab_button(self):
        """Clica no botão para abrir uma nova aba"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.NEW_TAB_BUTTON)
        ).click()

    def is_new_tab_opened(self):
        """Valida se a nova aba foi aberta e contém a mensagem esperada"""
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))  # Espera abrir a nova aba

        original_tab = self.driver.current_window_handle
        all_tabs = self.driver.window_handles

        for tab in all_tabs:
            if tab != original_tab:
                self.driver.switch_to.window(tab)
                break

        # Verifica se a mensagem esperada aparece
        page_text = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.PAGE_TEXT)
        ).text
        self.driver.close()  # Fecha a nova aba
        self.driver.switch_to.window(original_tab)  # Volta para a aba principal

        return "This is a sample page" in page_text