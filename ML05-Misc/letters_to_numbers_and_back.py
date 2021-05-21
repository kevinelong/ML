letter = "A"
print(ord(letter))  # GET THE ASCII/UTF-8

print(chr(65))
text = "0b1001011"
right_hand = text[2:]
print(right_hand)

###

name = "KEVIN"
for letter in name:
    print(ord(letter), str(bin(ord(letter)))[2:], str(hex(ord(letter)))[2:])

"""
please convert you own name to dec/bin/hex and observe the different slice capabilities perhaps changing the indexes in the biddle to slice at different points.
"""
