tuples_list = [(2, 9), (1, 8), (4, 7), (3, 6)]
 
# Sort the list by the last element of each tuple
tuples_list.sort(key=lambda x:x[-1])
 
# Print the sorted list
print("Sorted list:", tuples_list)



