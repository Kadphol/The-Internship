def calculate(question, guess, result, score):
    i = 0
    correct = 0
    if(guess in question): #check if guess is correct
        for c in question:
            if(guess == c):
                result[i] = c #show correct guess
                correct += 1 #add score
            i += 1
    else:
        result.append(guess) #append incorrect guess
    return result,score+correct



def main():
    question = []
    guess_count = 0
    score = 0
    while(True):
        question = input().split()
        try:
            [n for n in question if n.isdigit()] #check if question is number
            if(len(question) == 12): # check length of question
                break
            else:
                print("Must be 12 digits!")
        except ValueError:
            print("Number Only!")
    result = list('_' * len(question))
    print(' '.join(result))
    while(guess_count < 5):
        guess = input()
        try:
            check = int(guess)
            if(check < 0 or check > 9): #check range of guess
                print("Only 0 - 9")
            elif (guess in result): #check if number is already guess
                print("Already guess that number")
            else:
                guess_count += 1
                result,score = calculate(question,guess,result,score) #calculate score and result
                print('')
                print(' '.join(result)) #show result
        except ValueError:
            print("Please input number")
    print('')
    print(score)

if __name__ == '__main__':
    main()