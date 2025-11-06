#input from user
string = input("Enter the main string: ") 
substring = input("Enter the substring to check: ") 

# Check if substring is present in the string 
if substring in string: 
    print(f"The substring '{substring}' is present in the string.") 
else:
    print(f"The substring '{substring}' is not present in the string.")




