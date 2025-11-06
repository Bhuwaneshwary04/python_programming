#Input from the user
string = input("Enter a string: ") 
i = int(input("Enter the index of character to remove: ")) 

# Remove the i'th character using slicing
new_string = string[:i] + string[i+1:] 

# Output the result
print(f"The string after removing the character at index {i} is: {new_string}")


