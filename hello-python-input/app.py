import sys

def main():
    if len(sys.argv) > 1:
        print(f"Arguments passed in: {sys.argv[1:]}")
    else:
        print("Hello, world — no arguments passed.")

if __name__ == "__main__":
    main()
