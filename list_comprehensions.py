# [expression for item in list]

data = [11, 22, 33, 44]
output = [i for i in data]
print(data)

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)

# filtering example
data = [
    {"name": "aaa", "title": "SIONR IT ABC"},
    {"name": "bbb", "title": "SIONR ZZZ ABC"},
    {"name": "ccc", "title": "SIONR IT ABC"},
]

output = []

for e in data:
    if "IT" in e["title"]:
        output.append(e)

print(output)

# do it in one line with a list comprehension! ugly? hard to read? maybe.
print([e for e in data if "IT" in e["title"]])
