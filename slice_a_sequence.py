
text = "Now is the time for all good people to come to to the aid of their planet."
#A string is also a sequece like an array/list.

first = text[0]
print(first)

last = text[-1]
print(last)

middle_chunk = text[12:18] #SLICE : is the slice operator
print(middle_chunk)

"""
EXPECTED:
N
.
ime fo
"""

first_part = text[:18] # omit the beginning index so it start the very beginning
print(first_part)

last_part = text[18:] # omit the end index so it goes to the very end.
print(last_part)

duplicate = text[:] #make a true duplicate rather than copying the references

backward = text[::-1]
print(backward)

###

