import art

# Define functions to perform calculations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Initialise a dictionary of mathematical operators as keys and function names as values
operations = {}
keys = ["+", "-", "*", "/"]
values = [add, subtract, multiply, divide]
for key in keys:
    operations[key] = values[keys.index(key)]

# Call a function whose name corresponds to the key in operations dict
# and pass the user input as arguments to the function
def calculate(operation, n1, n2):
    if operation == "+":
        return operations["+"](n1, n2)
    elif operation == "-":
        return operations["-"](n1, n2)
    elif operation == "*":
        return operations["*"](n1, n2)
    elif operation == "/":
        return operations["/"](n1, n2)

def calculator():
    print(art.logo)
    n1 = int(input("Enter number 1: "))
    operation = input("Choose operation (type +, -, * or /): ")
    n2 = int(input("Enter number 2: "))
    result = calculate(operation, n1, n2)
    print(f"{n1} {operation} {n2} = {result}")

    # Loop to perform additional calculations
    while True:
        next_step = input("Type 'y' to perform another calculation, 'n' to start over: ").lower()
        if next_step == "y":
            n1 = result
            operation = input("Choose operation (type +, -, * or /): ")
            n2 = int(input("Enter number 2: "))
            result = calculate(operation, n1, n2)
            print(f"{n1} {operation} {n2} = {result}")
        else:
            print("\n" * 20)
            calculator()
            break


if __name__ == "__main__":
    calculator()






