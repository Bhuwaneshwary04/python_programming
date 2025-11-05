

# Take input for number of terms
terms = int(input("Enter the number of terms: "))

# Initialize first two Fibonacci numbers and a counter
a, b = 0, 1
count = 0

# Generate Fibonacci series using a while loop
while count < terms:
    print(a, end=' ')  # Print current number
    a, b = b, a + b    # Update values for next term
    count += 1         # Increment counter
