#Input string from the user 
string = input("Enter a string: ") 

# Split the string into words 
words = string.split()

# Loop through each word and check if its length is even
for word in words: 
    if len(word) % 2 == 0:
        print(word)
