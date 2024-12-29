def calculator():
    print("1. ADDITION (+)")
    print("2. SUBTRACTION (-)")
    print("3. MULTIPLY (*)")
    print("4. DIVISION (/)")
    print("e. Exit")
  
    while True:
        choice = input("Enter Choice (+, -, *, / or e to Exit): ")  # To input operation
        if choice == 'e':
            print("Exiting calculator.")
            break
        elif choice not in ['+', '-', '*', '/']:
            print("Enter a valid operation.")
            continue
        
        # If valid choice, proceed to input numbers
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        
        if choice == "+":
            result = num1 + num2
            print("Result:", result)
        elif choice == "-":
            result = num1 - num2
            print("Result:", result)
        elif choice == "*":
            result = num1 * num2
            print("Result:", result)
        elif choice == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)

calculator()
