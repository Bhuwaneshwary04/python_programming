student1 = [101, "Alice", "C001", "New York"]
student2 = [102, "Bob", "C002", "Los Angeles"]

#Concatenate the two lists
combined_students = student1 + student2

#Repeat the concatenated list 3 times using the * operator
repeated_students = combined_students * 3

#Print all the elements with their index using enumerate()
print("Students with index numbers:")
for index, student in enumerate(repeated_students):
    print(f"Index {index}: {student}")

#Add an address in student1 at the second position (index 1)
student1.insert(1, "Address: Unknown")
print("\nUpdated student1:", student1)
