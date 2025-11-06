string = input("Enter a string to check if it is a palindrome: ") 
# Reverse the string 
reversed_string = string[::-1] 
# Compare original and reversed strings 
if string == reversed_string: 
    print(f'"{string}" is a palindrome.') 
else: 
    print(f'"{string}" is not a palindrome.')


