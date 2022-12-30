# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).


def main():
    input_lines = []
    while True:
        try:
            l = input('> ')
            input_lines.append(l)
        except EOFError:
            break
    print('\n')
    for l in reversed(input_lines):
        print(l)

if __name__ == '__main__':
    main()
