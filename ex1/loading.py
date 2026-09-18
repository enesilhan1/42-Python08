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

