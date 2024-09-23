# Description: Examples of bitmask operations in Python.

# 1. Set a bit (Turn on a bit)
# Example: Turn on the 2nd bit of mask (indexing from 0)
mask = 0b0000  # Initial mask
i = 2
mask = mask | (1 << i)  # Set 2nd bit
print(f"Set the {i}-th bit: {bin(mask)}")  # Output: 0b100

# 2. Clear a bit (Turn off a bit)
# Example: Turn off the 2nd bit of mask
mask = 0b1100  # Initial mask
i = 2
mask = mask & ~(1 << i)  # Clear 2nd bit
print(f"Clear the {i}-th bit: {bin(mask)}")  # Output: 0b1000

# 3. Toggle a bit
# Example: Toggle the 2nd bit of mask
mask = 0b1100  # Initial mask
i = 2
mask = mask ^ (1 << i)  # Toggle 2nd bit
print(f"Toggle the {i}-th bit: {bin(mask)}")  # Output: 0b1000

# 4. Check if a bit is set
# Example: Check if the 2nd bit of mask is set
mask = 0b1100  # Initial mask
i = 2
is_set = mask & (1 << i)  # Check 2nd bit
print(f"Is the {i}-th bit set? {bool(is_set)}")  # Output: True

# 5. Check if a bit is clear
# Example: Check if the 1st bit of mask is clear
mask = 0b1100  # Initial mask
i = 1
is_clear = not (mask & (1 << i))  # Check 1st bit
print(f"Is the {i}-th bit clear? {bool(is_clear)}")  # Output: True

# 6. Count the number of set bits (Hamming weight)
# Example: Count set bits in mask
mask = 0b1100  # Initial mask
count = bin(mask).count("1")  # Count number of 1s
print(f"Number of set bits: {count}")  # Output: 2

# Alternative method:
mask = 0b1100  # Reset mask
count = 0
while mask:
    count += mask & 1  # Add if the lowest bit is set
    mask >>= 1  # Shift right by 1
print(f"Number of set bits (alternative): {count}")  # Output: 2

# 7. Get the lowest set bit
# Example: Isolate the lowest set bit in mask
mask = 0b1100  # Initial mask
lowest_set_bit = mask & -mask  # Get lowest set bit
print(f"Lowest set bit: {bin(lowest_set_bit)}")  # Output: 0b100

# 8. Turn off the lowest set bit
# Example: Turn off the lowest set bit in mask
mask = 0b1100  # Initial mask
mask = mask & (mask - 1)  # Clear lowest set bit
print(f"Turn off the lowest set bit: {bin(mask)}")  # Output: 0b1000

# 9. Get the index of the lowest set bit
# Example: Get the index of the lowest set bit in mask
mask = 0b1100  # Initial mask
index = (mask & -mask).bit_length() - 1  # Get index of lowest set bit
print(f"Index of lowest set bit: {index}")  # Output: 2

# 10. Subset generation (for all subsets of a set)
# Example: Generate all subsets of mask
mask = 0b1100  # Initial mask
subset = mask
print("Subsets of mask:")
while subset:
    print(f"{bin(subset)}")
    subset = (subset - 1) & mask  # Generate next subset

# 11. Iterate over all subsets of a given size
# Example: Generate all subsets of size 2 for a set of size 4
from itertools import combinations

n = 4  # Size of the set
k = 2  # Size of subsets
print(f"Subsets of size {k}:")
for combo in combinations(range(n), k):
    subset = sum(1 << i for i in combo)
    print(f"{bin(subset)}")

# 12. Check if one set is a subset of another
# Example: Check if A is a subset of B
A = 0b0100  # Subset
B = 0b1100  # Superset
is_subset = (A & B) == A
print(f"Is A a subset of B? {is_subset}")  # Output: True
