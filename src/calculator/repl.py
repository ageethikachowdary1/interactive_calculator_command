from calculator.operations import add, subtract, multiply, divide


def get_number(prompt: str) -> float:
    while True:
        text = input(prompt).strip()
        if text.lower() == "q":
            raise SystemExit
        try:
            return float(text)
        except ValueError:
            print("Invalid number. Enter a valid number like 3 or 3.5.")


def main() -> None:
    print("Simple Calculator")
    print("Type +  -  *  / to calculate")
    print("Type 'q' to quit")

    while True:
        op = input("\nEnter operation (+, -, *, / or q): ").strip().lower()

        if op == "q":
            print("Goodbye!")
            break

        if op not in {"+", "-", "*", "/"}:
            print("Invalid operation. Choose +, -, *, /.")
            continue

        try:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
        except SystemExit:
            print("Goodbye!")
            break

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        if isinstance(result, str):
            print("Error:", result)
        else:
            print("Result =", result)


if __name__ == "__main__":
    main()
