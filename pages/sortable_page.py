from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class SortablePage:
    URL = "https://demoqa.com/sortable"

    SORTABLE_ITEMS = (By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
    PAGE_TITLE = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Abre a página do Sortable"""
        self.driver.get(self.URL)

    def is_loaded(self):
        """Verifica se a página carregou corretamente"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PAGE_TITLE)
        )

    def get_list_items(self):
        """Retorna a lista de elementos na página"""
        return self.driver.find_elements(*self.SORTABLE_ITEMS)

    def get_reverse_sorted_list(self):
        """Retorna a lista de textos ordenados de forma decrescente"""
        items = self.get_list_items()
        return sorted([item.text for item in items], reverse=True)

    from selenium.webdriver.common.keys import Keys

    def sort_elements_descending(self):
        """Reorganiza todos os elementos na ordem decrescente (Six → Five → Four → Three → Two → One)."""
        action = ActionChains(self.driver)

        # Scroll para o final da página antes de começar a ordenar
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(1)  # Pequeno delay para permitir a atualização visual

        # Obtém os itens antes da movimentação
        items = self.get_list_items()
        ordem_atual = [item.text.strip() for item in items]
        ordem_desejada = ["Six", "Five", "Four", "Three", "Two", "One"]

        print(f"🔄 Ordem Inicial: {ordem_atual}")

        for posicao_correta, texto_elemento in enumerate(ordem_desejada):
            items = self.get_list_items()  # Atualiza os elementos a cada iteração
            item_positions = {item.text.strip(): index for index, item in enumerate(items)}

            if texto_elemento not in item_positions:
                print(f"⚠️ Elemento {texto_elemento} não encontrado!")
                continue  # Pula para o próximo item

            elemento_atual = items[item_positions[texto_elemento]]
            destino = items[posicao_correta]

            if item_positions[texto_elemento] != posicao_correta:
                print(f"🎯 Movendo {texto_elemento} para posição {posicao_correta}")

                # Move o elemento lentamente para evitar sobrescrever
                action.click_and_hold(elemento_atual).pause(0.2).move_to_element(destino).pause(0.5).release().perform()
                time.sleep(0.7)  # Pequeno delay para garantir sincronização

                # Reavaliar a posição antes de continuar
                items = self.get_list_items()
                nova_ordem = [item.text.strip() for item in items]
                print(f"🔍 Nova Ordem Após Mover {texto_elemento}: {nova_ordem}")

        # **Aguardar atualização antes de validar**
        WebDriverWait(self.driver, 3).until(lambda d: self.is_sorted_correctly_descending())

        print("✅ Elementos reordenados para ordem decrescente!")

    def is_sorted_correctly_descending(self):
        """Valida se os elementos estão na ordem decrescente esperada."""
        time.sleep(1)  # Pequena pausa para atualização da UI
        items = self.get_list_items()
        ordem_atual = [item.text.strip() for item in items]
        ordem_esperada = ["Six", "Five", "Four", "Three", "Two", "One"]

        print(f"🔍 Ordem Atual na UI: {ordem_atual}")
        print(f"✅ Ordem Esperada: {ordem_esperada}")

        if ordem_atual != ordem_esperada:
            time.sleep(1)  # Pequena pausa antes de uma segunda validação
            items = self.get_list_items()
            ordem_atual = [item.text.strip() for item in items]
            print(f"🔄 Ordem Atual Após Espera: {ordem_atual}")

        return ordem_atual == ordem_esperada

    def get_sorted_elements(self):
        """Retorna a lista de elementos na ordem atual da UI"""
        items = self.driver.find_elements(*self.SORTABLE_ITEMS)  # Mapeie corretamente os elementos
        return [item.text.strip() for item in items]  # Retorna a lista de textos ordenados