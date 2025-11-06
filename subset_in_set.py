# Create two sets
set1= {1, 2, 3, 4, 5}
set2= {2, 3, 4}

# Print both sets
print("Set 1:", set1)
print("Set 2:", set2)

# Check if set2 is a subset of set1
if set2.issubset(set1):
    print("\nSet 2 is a subset of Set 1")
else:
    print("\nSet 2 is NOT a subset of Set 1")

# Check the opposite (if set1is a subset of set2)
if set1.issubset(set2):
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is NOT a subset of Set 2")
