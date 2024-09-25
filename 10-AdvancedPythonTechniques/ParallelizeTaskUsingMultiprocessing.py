import multiprocessing

# Define a function that computes the square of a number
def compute_square(number):
    return number * number

# Define a function to parallelize the computation
def parallel_square(numbers):
    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        # Distribute the work across multiple processes
        results = pool.map(compute_square, numbers)
    return results

if __name__ == "__main__":
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the parallel function
    results = parallel_square(numbers)

    # Print the results
    print(f"Input numbers: {numbers}")
    print(f"Squared numbers: {results}")
