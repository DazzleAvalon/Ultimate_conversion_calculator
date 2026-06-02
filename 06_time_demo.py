time_dict = {
    "ms": 3600 * 1000,
    "s": 3600,
    "m": 60,
    "h": 1,
    "d": 1 / 24,
    "month": 1 / 168,
    "y": 1 / (24 * 365 + 6 + 9 /  60) # accounts for leap years
}

# Get amount and units (assume they are valid)
amount = float(input("Unit amount? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = time_dict[to_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = time_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")