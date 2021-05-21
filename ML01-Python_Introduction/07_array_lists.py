# Array of integers
numbers = [12, 23, 54]

# Array of Strings
names = [
    "Bob",
    "Carol",
    "Ted",
    "Alice"
]
print(numbers)
print(names)

# Declare an Array of Strings
names: [str] = []
# Append two items
names.append("Bob")
names.append("Carol")
assert (len(names) == 2)  # Verify
# Print Them Out
print(names[0])
print(names[1])
# Remove One Item
names.remove("Bob")
assert (len(names) == 1)  # Verify
