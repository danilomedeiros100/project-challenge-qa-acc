import random

from faker import Faker

faker = Faker()

def generate_valid_test_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "mobile": str(faker.random_int(min=6000000000, max=9999999999)),
        "subjects": "Maths",
        "address": faker.address().replace("\n", " "),
    }

def generate_weak_password_data():
    data = generate_valid_test_data()
    data["password"] = "12345"
    return data

def generate_mismatched_email_data():
    data = generate_valid_test_data()
    data["confirm_email"] = "wrong_email@example.com"
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