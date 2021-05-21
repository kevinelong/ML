# a Tuple is a read only list - Too-ple
data = (123, 456, 789)


# data[0] = 999 #replacing the value will fail

def get_many():
    return 111, 222, 333


data = get_many()

print(data)
print(type(data))

a, b, c = get_many()  # Unpacking into three separate variables
print(a)
print(b)
print(c)
