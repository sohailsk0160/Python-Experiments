# Take user input
num = int(input("Enter any number to find the sum of its digits: "))

# Initialize sum variable
s = 0  

# Loop to extract and sum digits
while num > 0:
    a = num % 10  # Extract the last digit
    s = s + a     # Add the digit to sum
    num = num // 10  # Remove the last digit

# Print the sum of digits
print("Sum of digits:", s)
