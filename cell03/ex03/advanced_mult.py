def main():
    for x in range(0, 11):
        print(f"Table de {x}:", end=" ")
        for y in range(0, 11):
            result = x * y
            print(f"{result}", end=" ")
        print()

main()