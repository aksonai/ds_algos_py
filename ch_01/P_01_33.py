# P-1.33 Write a Python program that simulates a handheld calculator. Your pro-
# gram should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each op-
# eration is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.


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
    print('Allowed operations are: "+", "-", "*", "/", "c" (to clear), "e" (to end)!')
    a = input('Number: ')
    while True:
        op = input('Operation: ')
        if op == 'e':
            break
        if op == 'c':
            a = input('Number: ')
            continue

        b = input('Number: ')
        a = perform_operation(float(a), float(b), op)
        if int(a) == a:
            a = int(a)
        print(a)


if __name__ == '__main__':
    calculate()
