import sys

def downcase_it(s: str) -> str:
    return s.lower()

def main():
    params = sys.argv[1:]

    if not params:
        print("none")
        return

    for p in params:
        print(downcase_it(p))

if __name__ == "__main__":
    main()