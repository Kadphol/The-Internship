"""
Sorting Acronyms
Input:  the first line contain integer N, the number of name input.
        the next N line contain string of name.
Output: Print the acronyms in each line with sorting by longest to shortest.
        if there are the same length, sorted by alphabetical order.
"""

def get_upper(name):
    word = []
    upper = ""
    word = name.split()
    for s in word:
        if(s[0].isupper()): #check if split word is upper
            upper+=s[0]
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
        acronym.append(get_upper(n)) #append acronym from each word 
    acronym.sort(key = lambda item: (-len(item),item)) #sort by alphabetical order and sort again by length with reverse order
    print("\n".join(acronym))

if (__name__ == "__main__"):
    main()