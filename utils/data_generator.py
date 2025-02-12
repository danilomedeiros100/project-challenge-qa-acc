import random

def generate_username():
    """Gera um nome de usuário único"""
    return f"usuario_teste_{random.randint(1000, 9999)}"

def get_default_password():
    """Retorna a senha padrão"""
    return "Teste@123"