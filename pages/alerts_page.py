from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/alerts"

    ALERT_BUTTON = (By.ID, "alertButton")

    def open(self):
        """Abre a página de Alerts"""
        self.driver.get(self.url)

    def click_alert_button(self):
        """Clica no botão para acionar o alerta"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ALERT_BUTTON)
        ).click()

    def is_alert_present(self):
        """Verifica se o alerta apareceu e contém a mensagem correta"""
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()  # Fecha o alerta
        return "You clicked a button" in alert_text