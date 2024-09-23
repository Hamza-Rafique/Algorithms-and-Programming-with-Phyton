# Define a memoization dictionary to store previously computed results
memo = {}

# Define the recursive Fibonacci function with memoization
def fibonacci(n):
    # Base case: return 1 if n is 1 or 2 (first two Fibonacci numbers)
    if n <= 1:
        return n
    
    # Check if the value is already computed and stored in the memo dictionary
    if n in memo:
        return memo[n]
    
    # Compute the Fibonacci number recursively and store the result in memo
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    
    return memo[n]

# Test the function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
