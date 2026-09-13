import sys
import site
import os


def is_it_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    package: list[str] = []
    try:
        package = site.getsitepackages()
    except Exception:
        pass

    if not is_it_venv():
        print("MATRIX STATUS: You're still plugged in")

        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print("Then run this program again")

        print("\nGlobal package installation path:")
        print("\n".join(package) if package else "Unavailable")
    else:
        venv: str = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")

        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {venv}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        print("\n".join(package) if package else "Unavailable")


if __name__ == "__main__":
    main()
