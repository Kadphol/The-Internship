"""
Floating Prime
Input:  input each decimal number between 1.0 to 10.0 (with number and decimal place not more than 12 digits).
        Checking if this decimal number are floating prime or not, program will continue until 0.0 is enter.
Output: TRUE if the number is floating prime, FALSE if it's not.
"""
def check_prime(number):
    if(number > 1):
        for i in range(2,number):
            if((number % i)==0):
                return False
        else:
            return True
    else:
        return False

def check_floating(number):
    checking = False
    for i in range (1,4):
        val = int(number * (10**i))
        if(check_prime(val)):
            checking = True
            break
    return checking

def main():
    while(True):
        number = input("Enter Float number: ")
        if(number == "0.0"):
            break
        try:
            val = float(number)
            if(val < 1.0 or val > 10.0):
                print("Floating Prime must be between 1.0 to 10.0")
            elif(len(number.replace(".",""))>12):
                print("Number and Decimal over 12 digits")
            else:
                if(check_floating(val)):
                    print("TRUE")
                else:
                    print("FALSE")
        except ValueError:
            print("Enter Float value")
        

if __name__ == "__main__":
    main()