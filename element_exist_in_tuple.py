#Create a tuple
tuple = (10, "Hello", 3.14, True, "Python")
print(tuple)

#Take input from the user
element = input("Enter the element to check: ")

#Convert input to proper type if needed (example: integer or float)
try:
    if '.' in element:
        element = float(element)
    else:
        element = int(element)
except ValueError:
    pass  # keep it as string if conversion fails

#Check if the element exists in the tuple
if element in tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
