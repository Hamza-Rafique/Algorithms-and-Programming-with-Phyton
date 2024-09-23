import time
from functools import wraps

# Decorator function to time another function
def time_it(func):
    @wraps(func)  # Preserves the metadata of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

# Example usage of the decorator
@time_it
def example_function(n):
    # A simple function that sleeps for n seconds
    time.sleep(n)
    return f"Slept for {n} seconds"

# Calling the decorated function
example_function(2)
