limit = int(input("Enter the limit: ")) 
total = 0 
for num in range(1, limit + 1): 
    total += num 
print(f"The sum of natural numbers up to {limit} is {total}.")
