import os
from dotenv import load_dotenv

def load_config() -> dict[str, str | None]:
    load_dotenv()
    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config

