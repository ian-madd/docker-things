import os

def main():
    name = os.environ.get("NAME", "World")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
