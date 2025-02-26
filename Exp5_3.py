# Function to check if a number is prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Example list
num_list = [10, 15, 17, 19, 21, 23, 30, 31, 35, 37]

# Filter out prime numbers
filtered_list = list(filter(lambda x: not is_prime(x), num_list))

# Print the result
print("List after filtering out prime numbers:", filtered_list)
