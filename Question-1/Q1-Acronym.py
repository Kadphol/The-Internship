def get_input(number):
    lines = []
    for i in range(number):
        line = input()
        lines.append(line)
    return(lines)


def main():
    number = int(input())
    name = get_input(number)
    print(name)

if (__name__ == "__main__"):
    main()