Number = int(input("Enter a number: "))


def CheckPrime(Number): 
    if Number >1:
        for i in range (2, Number):
            if(Number % i) == 0:
                print(Number, "is not a prime number")
                break
        else:
            print(Number, "is a prime number")
       
CheckPrime(Number)