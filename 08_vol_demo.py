vol_dict= {
    "ml": 1000 * 1000,
    "L": 1000,
    "kl": 1,
    "ML": .001,
}

# Get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = vol_dict[to_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = vol_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")