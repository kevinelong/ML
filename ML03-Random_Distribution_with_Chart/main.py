import random

result = random.randint(1, 6)
print(result)


# create a function that call roll quantity of dice, and the sides on each die.

def roll(quantity, sides):
    value = 0
    # TODO use for and range and random.randint
    for _ in range(quantity):
        value += random.randint(1, sides)
    return value


result = roll(3, 6)
print(result)

my_dict = {}
my_dict["foo"] = "bar"
print(my_dict["foo"])


# Create a function called roll_many that rolls 3 6-sided dice by calling the function above,
# but does so N times where N defaults to 100.

# Store the results in a dictionary that has the possible values (3-18) as the keys,
# and the number of times each possible value occured as the values.

def roll_many(n=500, quantity=3, sides=6):
    #     output = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0}
    output = {}

    # prepopulate with zeros keys 3-18
    for index in range(quantity, (quantity * sides) + 1):
        output[index] = 0

    # TODO
    for _ in range(n):
        value = roll(quantity, sides)
        output[value] += 1
    return output


result = roll_many()
print(result)


def roll_many2(n=500, quantity=3, sides=6):
    output = {}

    for _ in range(n):
        value = roll(quantity, sides)
        if value in output:
            output[value] += 1
        else:
            output[value] = 1
    return output


result2 = roll_many2()
print(result2)

# ISSUES: order is random for the keys and values of zero are missing


occurances = 12

for _ in range(occurances):
    print("#")

for _ in range(occurances):
    print("#", end="")
print("")

output = ""
for _ in range(occurances):
    output += "#"
print(output)

print("#" * 12)


def pad(n, minimum=2):
    text = str(n)
    while len(text) < minimum:
        text = " " + text
    return text


print(pad(9, 2))
print(pad(11, 2))


def pad2(n):
    if n < 10:
        return " " + str(n)
    else:
        return n


print(pad2(9))
print(pad2(11))


def pad3(n):
    return n if n > 9 else " " + str(n)
    # TERNARY or 3 way operator ? :


print(pad3(9))
print(pad3(11))

# Create a function called show_chart that takes the results from the function above and displays 16 rows numbered 3-18.
# a bar chart similar to this:
"""
 3: #####
 4: ######
 ...
17: ####
18: ###
"""


def show_chart(result):
    for item in result:
        value = result[item]
        print(f"{item:2}: {value * '#'}")


show_chart(result)


def show_chart2(result):
    for item in range(3, 19):
        value = result[item] if item in result else 0
        print(f"{item:2}: {value * '#'}")


show_chart2(result2)


# How can we make the chart scale if we do 1000 rather than 100 samples.

def pad(n, minimum=2):
    return f"{n:2}"


print(pad(9))
print(pad(11))


def zero_pad(n, minimum=2):
    return f"{n:02}"


print(zero_pad(9))
print(zero_pad(11))
