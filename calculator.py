def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero"
    return x / y

def calculator():
    print("------Simple Python Calculator-------")

    while True:
        print("\n Select an Operation.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice(1-5):")

        if choice in ( '1', '2', '3', '4'):
            try:
                x = float(input("Enter First Number:"))
                y = float(input("Enter second number:"))
            except ValueError:
                print("Invalid Input.")
                continue
        if choice == '1':
            print(f"Result = {x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"Result = {x} - {y} = {subtract(x, y)}")
        elif choice == '3':
            print(f"Result = {x} * {y} = {multiply(x, y)}")
        elif choice == '4':
            print(f"Result = {x} / {y} = {divide(x, y)}")
        elif choice == '5':
            print("Goodbye.")
            break
        else:
            print("Invalid Input.")

        
calculator()
        
            

    