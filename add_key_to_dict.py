new_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

#Take input for the new key and value
new_key = input("Enter the key to add: ")
new_value = input("Enter the value for the key: ")

#Convert value to integer if it represents a number
try:
    new_value = int(new_value)
except ValueError:
    pass  # keep it as string if conversion fails

#Add the new key-value pair to the dictionary
new_dict[new_key] = new_value

# Section 4: Print the updated dictionary
print("Updated dictionary:")
print(new_dict)
