def CheckStringPalindrome(input_string):
    # Slice the string with a step of -1 to reverse it
    if input_string == input_string[::-1]:
        return True
    else:
        return False
    

input_string = "racecar"

print(CheckStringPalindrome(input_string))