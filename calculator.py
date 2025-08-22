def calculator():
    print("Select operation: +  -  *  /")
    op = input("Enter operator: ").strip()
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator")

calculator()
