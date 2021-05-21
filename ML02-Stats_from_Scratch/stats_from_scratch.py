# Write a function that returns the total by adding a list of numbers together.
data = [123, 597, 631, 61, 93, 509]


def get_total(data):
    total = 0
    # TODO - Add code here-  for loop and add the item from the for loop to the total
    for item in data:
        total += item
    return total


print(get_total(data))


def get_average(data):
    total = 0
    # TODO - Add code here-  for loop and add the item from the for loop to the total
    for item in data:
        total += item
    return total / len(data)


print(get_average(data))


def get_largest(data):
    largest = data[0]
    # TODO - Add code here-  for loop and add the item from the for loop to the total
    for item in data:
        if item > largest:
            largest = item
    return largest


print(get_largest(data))


def get_smallest(data):
    smallest = data[0]
    # TODO - Add code here-  for loop and add the item from the for loop to the total
    for item in data:
        if item < smallest:
            smallest = item
    return smallest


print(get_smallest(data))

# next create functions that return the average, the largest, and then finally the smallest

# EXTRA create a class to hold the data and methods to operate on the shared data in the above way.
