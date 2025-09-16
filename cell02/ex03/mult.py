try:
    num_1 = int(input("Enter the first number: \n"))
    num_2 = int(input("Enter the second number: \n"))

    multresult = num_1 * num_2

    print(f"{num_1} x {num_2} = {multresult}")

    if (multresult == 0):
        print("The result is positive and negative.\n")
    elif (multresult > 0):
        print("The result is positive.\n")
    else:
        print("The result is negative.\n")
except:
    print("Error: invalid input.")