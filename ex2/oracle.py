import os
import sys
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

def print_config(config: dict[str, str | None]) -> None:
    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        print("Database: Connected")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")  

def main():
    print("ORACLE STATUS: Reading the Matrix...")
    config = load_config()
    errors = validate_config(config)
    if errors:
        for error in errors:
            print(f"Configuration Error: {error}")
        if config["MATRIX_MODE"] == "production":
            print("Cannot start in production without full configuration.")
            sys.exit(1)
        else:
            print("Running in development mode with incomplete configuration.")
    print_config(config)

if __name__ == "__main__":
    main()