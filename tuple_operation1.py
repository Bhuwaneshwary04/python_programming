Fruits = (1, 'banana', 2, 'apple', 3, 'cherry', 4, 'pineapple')

# Section 2: Print all elements using a for loop
print("All elements in Fruits tuple:")
for item in Fruits:
    print(item)

# Section 3: Print elements with their index using enumerate()
print("\nElements with index using enumerate():")
for index, item in enumerate(Fruits):
    print(f"Index {index}: {item}")

# Section 4: Create a list of cities
City = ['pune', 'nagar', 'nashik', 'mumbai']

# Section 5: Convert the City list into a tuple
City_tuple = tuple(City)
print("\nCity list converted to tuple:", City_tuple)

# Section 6: Concatenate Fruits and City_tuple
combined_tuple = Fruits + City_tuple
print("\nConcatenated tuple:", combined_tuple)

# Section 7: Repeat the City_tuple 4 times
repeated_city = City_tuple * 4
print("\nCity tuple repeated 4 times:", repeated_city)

# Section 8: Check whether "pune" exists in the City_tuple
is_pune_in_tuple = "pune" in City_tuple
print("\nIs 'pune' in the City tuple?", is_pune_in_tuple)
