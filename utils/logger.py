import logging

# Configuração global do Log
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S"
)

# Criar instância do logger para uso global
logger = logging.getLogger(__name__)