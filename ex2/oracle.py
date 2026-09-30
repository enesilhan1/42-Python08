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

def validate_config(config: dict[str, str | None]) -> list[str]:
    errors: list[str] = []
    if not config["DATABASE_URL"]:
        errors.append("DATABASE_URL is not set.")
    if not config["API_KEY"]:
        errors.append("API_KEY is not set.")
    if not config["ZION_ENDPOINT"]:
        errors.append("ZION_ENDPOINT is not set.")
    return errors

