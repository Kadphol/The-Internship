def check_prime(number): #checking prime number
    if(number > 1):
        for i in range(2,number):#find if number can modulo with any number
            if((number % i)==0):
                return False #if it can return false
        else:
            return True #if not return true
    else:
        return False

def check_floating(number):
    checking = False
    for i in range (1,4):
        val = int(number * (10**i)) #shift decimal place
        if(check_prime(val)):#check prime of number
            checking = True
            break
    return checking

def main():
    while(True):
        number = input("Enter Float number: ")
        if(number == "0.0"): #terminate program if input is '0.0'
            break
        try: #try if input is number or not
            val = float(number)
            if(val < 1.0 or val > 10.0): #check range of input
                print("Floating Prime must be between 1.0 to 10.0")
            elif(len(number.replace(".",""))>12): #check length of input
                print("Number and Decimal over 12 digits")
            else:
                if(check_floating(val)): #checking floating prime
                    print("TRUE")
                else:
                    print("FALSE")
        except ValueError:
            print("Enter Float value")
        

if __name__ == "__main__":
    main()