def sum_of_list(numbers):
    total = 0  # Initialize a variable to store the sum
    for num in numbers:  # Iterate through each number in the list
        total += num  # Add each number to the total
    return total
 
# Example usage
l=[]
n=int(input("enter how many elements:"))
for i in range (n):
    element=int(input("Enter the element"))
    l.append(element)
#numbers = [10, 20, 30, 40, 50]
result = sum_of_list(l)
print("The sum of the list is:", result)
