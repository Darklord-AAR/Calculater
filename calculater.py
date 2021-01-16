def calculater():
    print("\nWelcome to Faulty calculator")
    operation = input(
        "Please select math operation to perform, from below list:\n + For Addition\n - For Subtraction\n * "
        "For Multiplication\n / For Division\n ** For Power \n % For module\nEnter Your choice = ")
    if operation == "+":
        print("You Select Addition")
    if operation == "-":
        print("You Select Subtraction ")
    if operation == "*":
        print("You select Multiplication")
    if operation == "/":
        print("You Select Division")
    if operation == "**":
        print("You Select Power")
    if operation == "%":
        print("You Select Module")

    Number1 = int(input("Enter First Number -> "))
    Number2 = int(input("Enter Second Number -> "))

    if operation == "+":
        print(f"Addition is ")
        print(f"{Number1} + {Number2} = {Number1 + Number2}")
    elif operation == "-":
        print("Subtraction is")
        print(f"{Number1}-{Number2} = {Number1 - Number2}")
    elif operation == "*":
        print("Multiplication is")
        print(f"{Number1}*{Number2} = {Number1 * Number2}")
    elif operation == "/":
        print("Division is")
        print(f"{Number1}/{Number2} = {Number1 / Number2}")
    elif operation == "**":
        print("Power is")
        print(f"{Number1}**{Number2} = {Number1 ** Number2}")
    elif operation == "%":
        print("Module is")
        print(f"{Number1}%{Number2} = {Number1 % Number2}")
    else:
        print("You Press invalid key")
    again()


def again():
    cal_again = input("Do you want to calculate again? \n Please type Y for yes or N for no ")
    if cal_again == 'Y':
        calculater()
    elif cal_again == 'N':
        print("See you later \nThank You!")
    else:
        print("Invalid Key! ")
        again()

calculater()