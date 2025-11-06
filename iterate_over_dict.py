#Sample dictionary
new_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

#Iterate over keys
print("Iterating over keys:")
for key in new_dict:
    print(f"Key: {key}, Value: {new_dict[key]}")

#Iterate over values
print("\nIterating over values:")
for value in new_dict.values():
    print(f"Value: {value}")

#Iterate over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in new_dict.items():
    print(f"Key: {key}, Value: {value}")
