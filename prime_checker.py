# Input the number 
number = int(input("Enter a number: ")) 
# Check if the number is less than 2
if number < 2: 
           print("The number is not a prime number.") 
else: 
          # Check for factors from 2 to the number – 1
          for i in range(2, number): 
                   if number % i == 0: 
                            print("The number is not a prime number.") 
                            break 
          else: print("The number is a prime number.")


