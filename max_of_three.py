def find_max_of_three():
    # Accept user input for three numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    # Logic to find the maximum number without using max()
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
 
# Example usage
max_number = find_max_of_three()
print("The maximum number is:", max_number)
