def get_upper(name): #get acronym of name
    word = []
    upper = ""
    word = name.split()
    for s in word:
        if(s[0].isupper()): #check if split word is upper
            upper+=s[0]
    return upper

def get_input(number): #get input of name
    lines = []
    for i in range(number):
        line = input()
        lines.append(line)
    return(lines)

def main():
    while(True): #check if input is integer
        try:
            number = int(input())
            break
        except ValueError:
            print("Enter Number")
    name = get_input(number)
    acronym = []
    for n in name:
        acronym.append(get_upper(n)) #append acronym from each word 
    acronym.sort(key = lambda item: (-len(item),item)) #sort by alphabetical order and sort again by length with reverse order
    print("")
    print("\n".join(acronym))

if (__name__ == "__main__"):
    main()