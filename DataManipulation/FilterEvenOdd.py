def FilterEvenOdd(input_list):
    Odd = []
    Even = []
    for item in input_list:
        if item % 2 == 0:
            Even.append(item)
        else:
            Odd.append(item)
    return [Even, Odd]


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print(FilterEvenOdd(input_list))