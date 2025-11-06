"""Q.Inventory Management System
You are managing the inventory of a store that sells various products. The store uses a Python dictionary to track product names and their quantities in stock. The current inventory is as follows:
inventory = {
    "Laptop": 20,
    "Smartphone": 50,
    "Headphones": 30,
    "Keyboard": 15,
    "Mouse": 40
}
Perform the following operations on the inventory dictionary:
1.	Use clear() to remove all products from the inventory.
2.	Use copy() to create a backup of the current inventory.
3.	Use fromkeys() to create a new dictionary with product names as keys and set their quantities to 0.
4.	Use get() to check how many units of "Smartphone" are in stock.
5.	Use items() to print all products and their quantities in stock.
6.	Use keys() to list all the product names in the inventory.
7.	Use pop() to remove the "Keyboard" from the inventory and print how many units were in stock.
8.	Use popitem() to randomly remove a product from the inventory and print its name and quantity.
9.	Use setdefault() to add a new product "Tablet" with an initial stock of 10 units, if it doesn’t already exist.
10.	Use update() to add 20 more "Mouse" units or add a new product "Monitor" with 25 units if it doesn’t exist.
11.	Use values() to see the current quantities of all products in stock."""

# Initial inventory dictionary 
inventory = { "Laptop": 20, "Smartphone": 50, "Headphones": 30, "Keyboard": 15, "Mouse": 40 } 

# 1. Use copy() to create a backup of the current inventory
backup_inventory = inventory.copy() 
print("Backup Inventory:", backup_inventory) 

# 2. Use fromkeys() to create a new dictionary with product names as keys and set their quantities to 0 
new_inventory = dict.fromkeys(inventory.keys(), 0) 
print("New Inventory with quantities set to 0:", new_inventory) 

# 3. Use get() to check how many units of "Smartphone" are in stock 
smartphone_stock = inventory.get("Smartphone") 
print("Units of Smartphone in stock:", smartphone_stock)

# 4. Use items() to print all products and their quantities in stock 
print("All products and their quantities in stock:")
for product, quantity in inventory.items(): 
    print(f"{product}: {quantity}")
    
# 5. Use keys() to list all the product names in the inventory
print("Product names in the inventory:", list(inventory.keys())) 

# 6. Use pop() to remove the "Keyboard" from the inventory and print how many units were in stock
keyboard_stock = inventory.pop("Keyboard")
print("Removed 'Keyboard' from inventory, stock was:", keyboard_stock) 

# 7. Use popitem() to randomly remove a product from the inventory and print its name and quantity 
removed_product, removed_quantity = inventory.popitem() 
print(f"Randomly removed product: {removed_product}, Quantity: {removed_quantity}") 

# 8. Use setdefault() to add a new product "Tablet" with an initial stock of 10 units, if it doesn’t already exist 
inventory.setdefault("Tablet", 10)
print("Inventory after adding Tablet if not already present:", inventory) 

# 9. Use update() to add 20 more "Mouse" units or add a new product "Monitor" with 25 units if it doesn’t exist 
inventory.update({"Mouse": inventory.get("Mouse", 0) + 20, "Monitor": 25})
print("Inventory after updating Mouse and adding Monitor:", inventory) 

#10. Use values() to see the current quantities of all products in stock 
print("Current quantities of all products in stock:", list(inventory.values()))
