def get_upper(name):
    word = []
    upper = ""
    word = name.split()
    for s in word:
        if(s[0].isupper()):
            upper+=s[0]
    print(upper)
    return upper

def get_input(number):
    lines = []
    for i in range(number):
        line = input()
        lines.append(line)
    return(lines)


def main():
    number = int(input())
    name = get_input(number)
    acronym = []
    for n in name:
        acronym.append(get_upper(n))
    

if (__name__ == "__main__"):
    main()