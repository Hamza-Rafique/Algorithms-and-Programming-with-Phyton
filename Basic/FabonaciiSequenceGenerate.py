# def FabonaciiSequenceGenerate(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return FabonaciiSequenceGenerate(n-1) + FabonaciiSequenceGenerate(n-2) 
       

# print(FabonaciiSequenceGenerate(10))

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_terms = 10
print(fibonacci(num_terms))
