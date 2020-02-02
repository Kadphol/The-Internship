def get_input(number):
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    print(lines)


def main():
    number = input()
    get_input(number)

if (__name__ == "__main__"):
    main()