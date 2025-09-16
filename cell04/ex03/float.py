def main():
    try:
        num = float(input("Give me a number: "))
        if num.is_integer():
            print("This number is an integer.") # check int >>> int
        else:
            print("This number is a decimal.") # >>> no int
    except ValueError:
        print("Error: invalid input.")

main()
