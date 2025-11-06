
#Create a sample dictionary
my_dict = {'apple': 50, 'banana': 20, 'cherry': 30, 'date': 40}

#Sort dictionary by value in ascending order
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by value (ascending):")
print(sorted_asc)

#Sort dictionary by value in descending order
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("\nDictionary sorted by value (descending):")
print(sorted_desc)
