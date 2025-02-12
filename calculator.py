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

def matrix_addition(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtraction(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

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
print("6. Matrix Addition")
print("7. Matrix Subtraction")
print("8. Matrix Multiplication")

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
    elif choice in ('6', 'matrix addition', '7', 'matrix subtraction', '8', 'matrix multiplication'):
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print("Enter elements for first matrix:")
        A = [[float(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
        print("Enter elements for second matrix:")
        B = [[float(input(f"B[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

        if choice == '6' or choice == 'matrix addition':
            result = matrix_addition(A, B)
            operation = f"Matrix Addition:\n{A}\n+\n{B}\n=\n{result}"
        elif choice == '7' or choice == 'matrix subtraction':
            result = matrix_subtraction(A, B)
            operation = f"Matrix Subtraction:\n{A}\n-\n{B}\n=\n{result}"
        elif choice == '8' or choice == 'matrix multiplication':
            result = matrix_multiplication(A, B)
            operation = f"Matrix Multiplication:\n{A}\n*\n{B}\n=\n{result}"

        print(operation)
        history.append(operation)

    else:
        print("Invalid input...Pls try again...")
        continue

    next_problem = input("Let's do another calculation? (yes/no): ")
    if next_problem.lower() == "no":
        break

