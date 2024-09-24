def nth_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)  

print(nth_fibonacci(10))
