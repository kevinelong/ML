text = input("How old are you? (Enter a whole number. e.g. 21)")
age = int(text)  # convert text to integer type

if age < 21:
    print("May Not Drink.")
elif age < 35:
    print("May drink.")
elif age < 65:
    print("Should not drink.")
else:
    print("Why Not Drink.")
print("All done!")
