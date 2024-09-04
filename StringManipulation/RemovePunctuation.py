def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))


input_string = "Hello, World! How are you?"

print(remove_punctuation(input_string))