import random

from faker import Faker


faker = Faker()

def generate_valid_test_data():
    """Gera dados aleatórios válidos para preencher o formulário"""
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "gender": random.choice(["Male", "Female", "Other"]),
        "mobile": f"{random.randint(6000000000, 9999999999)}",
        "subjects": "Maths",
        "address": faker.address().replace("\n", " "),
        "state": "NCR",
        "city": "Delhi"
    }

def generate_weak_password_data():
    data = generate_valid_test_data()
    data["password"] = "12345"
    return data

def generate_mismatched_email_data():
    """Gera dados para testar e-mails diferentes"""
    data = generate_valid_test_data()
    if "confirm_email" in data:
        data["confirm_email"] = "wrong_email@example.com"  # Se o campo existir
    return data

def generate_incomplete_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": "",
        "mobile": "",
        "subjects": "",
        "address": "",
    }

def generate_username():
    """Gera um nome de usuário único"""
    return f"usuario_teste_{random.randint(1000, 9999)}"


def get_default_password():
    """Retorna a senha padrão"""
    return "Teste@123"

def generate_valid_web_tables_data():
    """Gera dados válidos para o formulário Web Tables"""
    fake = Faker()
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": str(random.randint(18, 65)),
        "salary": str(random.randint(30000, 120000)),
        "department": fake.job()
    }
print(generate_valid_web_tables_data())