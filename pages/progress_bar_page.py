import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProgressBarPage:
    """Page Object para a página de Progress Bar"""

    URL = "https://demoqa.com/progress-bar"

    # Elementos
    START_BUTTON = (By.ID, "startStopButton")
    RESET_BUTTON = (By.ID, "resetButton")
    PROGRESS_BAR = (By.CLASS_NAME, "progress-bar")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Abre a página do Progress Bar"""
        self.driver.get(self.URL)

    def is_loaded(self):
        """Verifica se a página carregou corretamente"""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.START_BUTTON))

    def click_start_button(self):
        """Clica no botão Start"""
        self.driver.find_element(*self.START_BUTTON).click()

    def click_reset_button(self):
        """Clica no botão Reset"""
        self.driver.find_element(*self.RESET_BUTTON).click()



    def get_progress_value(self):
        """Obtém o valor numérico da progress bar com tratamento de erro"""
        for _ in range(5):  # Tentativa de 5 vezes para capturar o valor correto
            progress_text = self.driver.find_element(*self.PROGRESS_BAR).text.strip()
            if progress_text:  # Garante que não está vazio
                return int(progress_text.replace('%', ''))
            time.sleep(0.5)  # Pequeno delay para esperar atualização do DOM
        return 0  # Retorna 0 caso não consiga capturar um valor válido

    def stop_progress_before(self, limit=25):
        """Aguarda até que o progresso atinja o limite e então clica em Stop"""
        while True:
            progress = self.get_progress_value()

            print(f"🔄 Monitorando progresso: {progress}%")  # Log para depuração

            if progress >= limit - 1:  # Pequena margem para evitar ultrapassar
                print("🛑 Parando o progresso...")  # Log para depuração
                self.click_stop_button()
                time.sleep(0.3)  # Pequeno delay para garantir que o clique foi processado

                # Confirma que o progresso realmente parou
                final_progress = self.get_progress_value()
                if final_progress >= limit - 1:
                    print(f"✅ Progresso interrompido corretamente em {final_progress}%")
                    break

            time.sleep(0.1)  # Pequeno delay para evitar sobrecarga do loop

    def click_stop_button(self):
        """Clica no botão Stop (que é o mesmo botão Start)"""
        self.driver.find_element(*self.START_BUTTON).click()

    def wait_until_complete(self):
        """Aguarda até que a progress bar atinja 100%"""
        while True:
            progress = self.get_progress_value()
            print(f"🔄 Monitorando progresso: {progress}%")  # Log para depuração

            if progress >= 100:
                print("✅ Progresso atingiu 100%!")
                break  # Sai do loop quando atingir 100%

            time.sleep(0.1)  # Pequeno delay para evitar sobrecarga no loop