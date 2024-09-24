def FindAllPermutationsString(input_string):
    if len(input_string) == 1:
        return [input_string]
    else:
        permutations = []
        for i in range(len(input_string)):
            char = input_string[i]
            remaining_string = input_string[:i] + input_string[i+1:]
            remaining_permutations = FindAllPermutationsString(remaining_string)
            for permutation in remaining_permutations:
                permutations.append(char + permutation)
        return permutations
    

input_string = "abc"

print(FindAllPermutationsString(input_string))