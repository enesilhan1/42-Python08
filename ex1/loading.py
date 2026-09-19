from importlib.metadata import version, PackageNotFoundError

DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def get_version(name: str) -> str | None:
    try:
        return (version(name))
    except PackageNotFoundError:
        return

def check_dependencies() -> list[str]:
    missings: list[str] = []
    for name, description in DEPENDENCIES.items():
        vs = get_version(name)
        if vs:
            print(f"[OK] {name} ({vs}) - {description}")
        else:
            print(f"[KO] {name} missing")
            missings.append(name)
    return missings


def print_install_instructions() -> None:
    print("\nInstalling with pip")
    print("pip install -r requirements.txt")

    print("\nInstalling with Poetry")
    print("poetry install")
    print("poetry run python loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    missing = check_dependencies()
    if missing:
        print_install_instructions()
        return


if __name__ == "__main__":
    main()
