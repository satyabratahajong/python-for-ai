def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == "5":
            print("Exiting calculator.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if choice == "1":
            res = add(num1, num2)
            op = "+"
        elif choice == "2":
            res = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            res = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            res = divide(num1, num2)
            op = "/"

        print(f"Result: {num1} {op} {num2} = {res}")

if __name__ == "__main__":
    calculator()