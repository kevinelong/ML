coin_quantities = {}

coin_quantities[1] = 5  # We have 5 pennies
coin_quantities[5] = 4  # We have 4 nickels
coin_quantities[10] = 3  # We have 3 dimes
coin_quantities[25] = 2  # We have 2 quarters

quarter_count = coin_quantities[25]
print(quarter_count)
assert (2 == quarter_count)
