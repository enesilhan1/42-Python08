import sys
import site


def is_it_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
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




if __name__ == "__main__":
    main()
