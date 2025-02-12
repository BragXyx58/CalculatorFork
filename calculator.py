# Calculator
# trial calculator
# licenced by Praneet .
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error. Division by zero."
    return x / y

history = []

print("Hey Hii!!")
print("Its a calculator made by Praneet Bose. ")
print("So now lets start -")
print("Select the method .")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5. View History")

while True:
    choice = input("Enter the choice of CALCULATION: ")

    if choice in ('1', 'add', '2', 'subtract', '3', 'multiply', '4', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1' or choice == 'add':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2' or choice == 'subtract':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3' or choice == 'multiply':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4' or choice == 'divide':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"

        print(operation)
        history.append(operation)

    elif choice == '5' or choice.lower() == 'history':
        print("\nCalculation History:")
        if history:
            for record in history:
                print(record)
        else:
            print("No calculations yet.")

    else:
        print("Invalid input...Pls try again...")
        continue

    next_problem = input("Let's do another calculation? (yes/no): ")
    if next_problem.lower() == "no":
        break

