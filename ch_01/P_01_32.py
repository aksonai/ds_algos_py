# P-1.32 Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.

def perform_operation(a: float, b: float, operation: str) -> float:
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b


def calculate() -> None:
    a = input('Enter the 1st number: ')
    op = input('Enter one of the operations +, -, *, / : ')
    b = input('Enter the 2nd number: ')
    result = perform_operation(float(a), float(b), op)
    if int(result) == result:
        result = int(result)
    print(result)


if __name__ == '__main__':
    calculate()
