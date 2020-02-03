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
    print(number)

def main():
    while(True):
        number = input()
        try:
            val = float(number)
            if(number == "0.0"):
                break
            else:
                check_floating(val)
        except ValueError:
            print("Enter Float value")
        

if __name__ == "__main__":
    main()