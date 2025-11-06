"""Q .Create a dictionary of employee data having keys like name, age and empid. And perform the following operations:
1.	Print all the keys.
2.	Print all the values
3.	Print all the key-value pair
4.	Print the value using key.
5.	Update the value of an existing key.
6.	Remove an entry, using del
7.	Check for the key existence. Using if  """


employee_data = { 'name': 'John Doe', 'age': 30, 'empid': 'E12345' } 
# 1. Print all the keys
keys = employee_data.keys() 
print("All keys:", keys)

 # 2. Print all the values 
values = employee_data.values() 
print("All values:", values) 

# 3. Print all the key-value pairs 
key_value_pairs = employee_data.items() 
print("All key-value pairs:", key_value_pairs)

# 4. Print the value using a specific key ('name') 
name_value = employee_data['name'] 
print("Value of 'name':", name_value)

# 5. Update the value of an existing key ('age') 
employee_data['age'] = 31
print("Updated employee data:", employee_data)
 
# 6. Remove an entry using `del` (removing 'empid')
del employee_data['empid'] 
print("Employee data after removal:", employee_data) 

# 7. Check for the key existence using `if` (check if 'age' exists)
if 'age' in employee_data:
    print("'age' exists in the employee data") 
else:
    print("'age' does not exist in the employee data")


