"""Q. Set Operations on Product Categories
You are managing two categories of products in a store: Electronics and Accessories.
The products in each category are stored in sets as follows:
electronics = {"Laptop", "Smartphone", "Tablet", "Smartwatch"}
accessories = {"Headphones", "Keyboard", "Mouse", "Smartwatch", "Charger", "Laptop"}

Perform the following set operations:
1. Use add() to add "Monitor" to the electronics set.
2. Use remove() to remove "Headphones" from the accessories set.
3. Use discard() to remove "Charger" from the accessories set.
4. Use union() to create a set that contains all products from both electronics and accessories.
5. Use intersection() to create a set of products that are present in both electronics and accessories.
6. Use difference() to find products that are in electronics but not in accessories.
7. Use symmetric_difference() to find products that are in either electronics or accessories, but not in both.
"""

# Initial product categories in sets
electronics = {"Laptop", "Smartphone", "Tablet", "Smartwatch"} 
accessories = {"Headphones", "Keyboard", "Mouse", "Smartwatch", "Charger", "Laptop"} 

# 1. Use add() to add "Monitor" to the electronics set
electronics.add("Monitor")
print("Electronics after adding Monitor:", electronics)

# 2. Use remove() to remove "Headphones" from the accessories set
accessories.remove("Headphones")
print("Accessories after removing Headphones:", accessories)

# 3. Use discard() to remove "Charger" from the accessories set
accessories.discard("Charger")
print("Accessories after discarding Charger:", accessories)

# 4. Use union() to create a set that contains all products from both electronics and accessories
all_products = electronics.union(accessories)
print("All products (union of electronics and accessories):", all_products)

# 5. Use intersection() to create a set of products that are present in both electronics and accessories
common_products = electronics.intersection(accessories)
print("Common products (intersection of electronics and accessories):", common_products)

# 6. Use difference() to find products that are in electronics but not in accessories
electronics_not_in_accessories = electronics.difference(accessories)
print("Products in electronics but not in accessories:", electronics_not_in_accessories)

# 7. Use symmetric_difference() to find products that are in either electronics or accessories, but not in both
exclusive_products = electronics.symmetric_difference(accessories)
print("Exclusive products (in either electronics or accessories, but not both):", exclusive_products)
