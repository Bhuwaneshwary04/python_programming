
num = int(input("Enter a number: "))


original_num = num
reverse = 0

while num > 0:
    digit = num % 10         
    reverse = reverse * 10 + digit 
    num //= 10               

if original_num == reverse:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
