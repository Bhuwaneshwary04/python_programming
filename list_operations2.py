# Initial list of elements
numbers = [82, 44, 120, 44, 12, 61, 44] 

# 1. Print the total of all the elements
total = sum(numbers) 
print(f"Total of all elements: {total}") 

# 2. Sort the list in ascending order 
numbers.sort() 
print(f"Sorted list: {numbers}") 

# 3. Remove the second element (with its value) 
numbers.pop(1) 

# Removes element at index 1 
print(f"List after removing the second element: {numbers}") 

# 4. Remove the first occurrence of the element 44 
numbers.remove(44) 

# Removes the first occurrence of 44
print(f"List after removing the first occurrence of 44: {numbers}") 

# 5. Pop the last element in the list and print it 
popped_element = numbers.pop() 

# Pops the last element 
print(f"Popped last element: {popped_element}") 
print(f"List after popping the last element: {numbers}") 

# 6. Insert 100 at the third position 
numbers.insert(2, 100) 

# Inserts 100 at index 2 (third position) 
print(f"List after inserting 100 at the third position: {numbers}") 

# 7. Add 200 at the end of the list
numbers.append(200)
print(f"List after adding 200 at the end: {numbers}")

 # 8. Calculate the total length of the list and print it
length = len(numbers)
print(f"Total length of the list: {length}") 

# 9. Print the index number of 200 
index_200 = numbers.index(200) 
print(f"Index of 200: {index_200}")

# 10. Count the total occurrences of 44 
count_44 = numbers.count(44) 
print(f"Total occurrences of 44: {count_44}") 

# 11. Reverse the list and print it 
numbers.reverse()
print(f"List after reversing: {numbers}")
