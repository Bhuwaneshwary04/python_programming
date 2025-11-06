def get_unique_elements(input_list):
    return list(set(input_list))
l=[] 
n=int(input("enter how many elements:")) 
for i in range (n): 
     element=int(input("Enter the element")) 
     l.append(element) 
print("List with duplicates",l)
unique_elements = get_unique_elements(l)
print("List with unique elements:", unique_elements)
