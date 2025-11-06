def count_case_letters(input_string):
    upper_count = 0  # Initialize a counter for uppercase letters
    lower_count = 0  # Initialize a counter for lowercase letters
    
    # Loop through each character in the input string
    for char in input_string:
        if char.isupper():  # Check if the character is uppercase
            upper_count += 1
        elif char.islower():  # Check if the character is lowercase
            lower_count += 1
    
    return upper_count, lower_count
 
input_str = input("Enter a string: ")
upper, lower = count_case_letters(input_str)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
