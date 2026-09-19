from importlib.metadata import version, PackageNotFoundError
import sys

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


def generate_matrix_data() -> "pd.DataFrame":
    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(42)
    sectors = rng.choice(["Zion", "Matrix", "Construct", "Nebuchadnezzar"], size=1000)
    signal = rng.normal(loc=50, scale=15, size=1000)

    df = pd.DataFrame({
        "sector": sectors,
        "signal": signal,
    })
    return df


def analyze_matrix_data(df: "pd.DataFrame") -> "pd.Series":
    print(f"\nProcessing {len(df)} data points...")
    by_sector = df.groupby("sector")["signal"].mean()
    return by_sector


def create_visualization(stats: "pd.Series") -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    stats.plot(kind="bar")
    plt.title("Matrix Signal Strength by Sector")
    plt.xlabel("Sector")
    plt.ylabel("Average Signal")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")



def compare_environments() -> None:
    print("\nEnvironment comparison:")
    print(f"Active environment: {sys.prefix}")
    if "pypoetry" in sys.prefix:
        print("Managed by: Poetry (poetry.lock pins exact versions)")
    else:
        print("Managed by: pip/venv (requirements.txt lists direct deps only)")
    print("\nInstalled versions:")
    for name in DEPENDENCIES:
        print(f"  {name}: {get_version(name)}")

def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    missing = check_dependencies()
    if missing:
        print_install_instructions()
        return
    df = generate_matrix_data()
    stats = analyze_matrix_data(df)
    create_visualization(stats)
    compare_environments()


if __name__ == "__main__":
    main()
