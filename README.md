# Projeto: Automação de Testes com Pytest-BDD

## 📌 Descrição do Projeto
Este projeto realiza testes automatizados de API utilizando **Python, Pytest-BDD, Requests** e **Allure Reports**. Os testes validam a funcionalidade da API do **DemoQA**.

## 📂 Estrutura do Projeto
```bash
project-challenge-qa-acc/
├── tests/
│   ├── api/
│   │   ├── test_create_user.py
│   │   ├── test_auth.py
│   │   ├── test_books.py
│   │   ├── test_reservation.py
│   │   ├── test_user_details.py
│   ├── features/
│   │   ├── api_create_user.feature
│   │   ├── api_auth.feature
│   │   ├── api_books.feature
│   │   ├── api_reservation.feature
│   │   ├── api_user_details.feature
├── utils/
│   ├── api_client.py      # Métodos reutilizáveis para chamadas à API
│   ├── data_generator.py  # Geração de dados dinâmicos
│   ├── config.py          # Configurações globais (URLs, headers)
├── conftest.py  # Configuração do pytest (fixtures globais)
├── pytest.ini  # Configuração do pytest
├── requirements.txt  # Dependências do projeto
├── reports/  # Relatórios do Allure
├── README.md  # Documentação do projeto
```

## 📦 Configuração do Ambiente
### Requisitos
- Python 3.8+
- `pip` instalado
- Git instalado

### 🛠️ Instalação no **Mac/Linux**
```bash
# Clonar o repositório
git https://github.com/danilomedeiros100/project-challenge-qa-acc.git

cd project-challenge-qa-acc

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 🛠️ Instalação no **Windows**
```powershell
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## 🚀 Execução dos Testes
### Rodar todos os testes
```bash
pytest --alluredir=reports
```

### Rodar um teste específico
```bash
pytest tests/api/test_create_user.py --alluredir=reports
```

### Gerar e visualizar os relatórios no Allure
```bash
allure serve reports
```

## 🌍 Configurações Globais
As configurações da API são mantidas no arquivo `utils/config.py`:
```python
BASE_URL = "https://demoqa.com"
```

## 📜 Boas Práticas
✔ Métodos reutilizáveis estão centralizados em `utils/api_client.py`  
✔ Dados dinâmicos são gerados em `utils/data_generator.py`  
✔ Os testes são organizados em arquivos separados por funcionalidade  
✔ Utilizamos `pytest-bdd` para testes baseados em BDD  
✔ Geração automática de relatórios detalhados com `Allure`

## 🛠️ Debugging e Solução de Problemas
### Caso o pytest não encontre a feature:
```bash
pytest --rootdir=. --cache-clear tests/api/test_create_user.py
```

### Caso haja erro ao rodar o Allure:
```bash
# Verifique se o Allure está instalado globalmente
allure --version

# Se não estiver instalado, instale com:
brew install allure  # MacOS
scoop install allure # Windows
```

## 📌 Contribuições
Sinta-se à vontade para contribuir! Basta abrir uma issue ou enviar um Pull Request.

---

📢 **Dúvidas ou sugestões? Entre em contato!** 🚀
