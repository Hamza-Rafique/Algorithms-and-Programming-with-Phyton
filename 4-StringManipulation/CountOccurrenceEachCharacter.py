def CountEachCharacter(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


input_string = "Hello World"

print(CountEachCharacter(input_string))