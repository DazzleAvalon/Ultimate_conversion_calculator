mass_dict= {
    "mg": 1000 * 1000,
    "g": 1000,
    "kg": 1,
    "T": .001,
}

# Get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = mass_dict[to_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = mass_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")