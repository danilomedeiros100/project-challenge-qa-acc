import logging

# Configuração global do Log
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.ERROR,  # Alterado de DEBUG para ERROR (ou WARNING, INFO, CRITICAL)
    datefmt="%H:%M:%S"
)

# Criar instância do logger para uso global
logger = logging.getLogger(__name__)

# Garantir que o logger use o mesmo nível global
logger.setLevel(logging.ERROR)  # Altere para WARNING, INFO ou CRITICAL conforme necessário