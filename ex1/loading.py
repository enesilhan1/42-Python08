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


