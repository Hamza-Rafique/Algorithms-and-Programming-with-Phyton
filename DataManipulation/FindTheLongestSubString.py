def FindTheLongestSubString(input_string):
    longest_string = ""
    current_string = ""
    for char in input_string:
        if char not in current_string:
            current_string += char
        else:
            if len(current_string) > len(longest_string):
                longest_string = current_string
            current_string = ""
            current_string += char
    if len(current_string) > len(longest_string):
        longest_string = current_string
    return longest_string

input_string = "abcabcbb"

print(FindTheLongestSubString(input_string))