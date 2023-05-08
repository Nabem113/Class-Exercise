from Math import Math
from Physics import Physics


print('''
What operation do you want to perform
Enter M for Math or P for Physics''')
calculation = input("> ").upper()

if calculation == "M":
    math_operation = Math()
    print('''
    What mathmatical operation would you like to perform? (input below)
    Enter;
    S for square
    A for Addition
    Su for subtraction
    M for muliplication
    D for division
    ''')
    choice_operation = input("> ")

    if choice_operation == "S":
        print("Enter number")
        number = int(input("> "))
        output = math_operation.square(number)
        print(output)

    elif choice_operation == "A":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = math_operation.addition(number1, number2)
        print(output)

    elif choice_operation == "SU":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = math_operation.subtraction(number1, number2)
        print(output)

    elif choice_operation == "M":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = math_operation.multipication(number1, number2)
        print(output)

    elif choice_operation == "D":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = math_operation.division(number1, number2)
        print(output)


elif calculation == "P":
    physics_operation = Physics()
    print('''
    What Physics operation would you like to perform? (input below)
    Enter;
    V to calculate velocity
    M to calculate momentum
    W to calculate weight
    Wd to calculate workdone
    D to calculate density
    ''')
    operation_choice = input("> ").upper()

    if operation_choice == "V":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = physics_operation.velocity(number1, number2)
        print(output)

    elif operation_choice == "M":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = physics_operation.momentum(number1, number2)
        print(output)

    elif operation_choice == "W":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = physics_operation.weight(number1, number2)
        print(output)

    elif operation_choice == "WD":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = physics_operation.workdone(number1, number2)
        print(output)

    elif operation_choice == "D":
        print("Enter first number")
        number1 = int(input("> "))
        print("Enter second number")
        number2 = int(input("> "))
        output = physics_operation.density(number1, number2)
        print(output)

else:
    print("Please enter valid input")