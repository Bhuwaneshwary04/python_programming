#Take input from the user
n = int(input("Enter the value of n: "))

#Create the dictionary using dictionary comprehension
squares_dict = {x: x*x for x in range(1, n+1)}

#Print the dictionary
print("Dictionary of numbers and their squares:")
print(squares_dict)
