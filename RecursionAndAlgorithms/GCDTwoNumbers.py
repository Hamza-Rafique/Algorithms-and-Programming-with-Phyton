def gcd_two_numbers(number1, number2):
    if number2 == 0:
        return number1
    else:
        return gcd_two_numbers(number2, number1 % number2)
    

print(gcd_two_numbers(15, 5))
