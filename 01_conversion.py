# Generates headings (eg:---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Welcome to the Ultimate conversion calculator!
- Please enter a unit you want converted from and to
- Mass (eg: 50 g to kg) unit options: mg, g, kg, T
- Time (eg: 300 seconds to hours) unit options: ms, s, m, h, d, month, y 
- Distance (eg: 500mm to m) unit options: mm, cm, m, km
-Volume(eg: 30L to ML) unit options: ml, L, kl, ML 

-Please convert using the same units! It will not work otherwise

To exit the program, just type "xxx"

("Have fun!")
   ''')

# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions " 
                          "or any key to continue ")

if want_instructions == "":
    instructions()

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

# Get amount and units (assume they are valid)
amount = float(input("Unit amount? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = distance_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")

time_dict = {
    "ms": 3600 * 1000,
    "s": 3600,
    "m": 60,
    "h": 1,
    "d": 1 / 24,
    "month": 1 / 168,
    "y": 1 / (24 * 365 + 6 + 9 / 60) # accounts for leap years
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

print(f"Thank you for using the ultimate conversion calculator!")

while True:
        if amount == "xxx":
            break

print("Have fun!")

