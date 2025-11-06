#Input from the user 
string1 = input("Enter the first string: ") 
string2 = input("Enter the second string: ") 

# Initialize a variable to count matching characters 
matching_count = 0 

# Loop through each character in the first string
for char in string1: 
    if char in string2: 
         matching_count += 1 
         
# Remove the first occurrence to avoid double counting
string2 = string2.replace(char, "", 1)
# Output the result 

print(f"Number of matching characters: {matching_count}")

