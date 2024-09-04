def longest_string(input_string):
    return max(input_string, key=len)


input_string = "abcabcbb"

print(longest_string(input_string))
