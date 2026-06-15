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
- Time (eg: 300 s to h) unit options: ms, s, min, h, d, month, y 
- Distance (eg: 500 mm to m) unit options: mm, cm, m, km

-Please no cross converting units
To exit the program, just type "xxx"

("Have fun!")
   ''')

# Main routine goes here

statement_generator("The ultimate conversion calculator" ,"-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions " 
                          "or any key to continue ")

if want_instructions == "":
    instructions()
def num_check(question):
    error = "you chose to continue\n"
    while True:

        response = input(question).lower
        if response == "xxx":
            return response

        try:
            # ask user for a number
            response = int(response)
        except ValueError:
            print(error)

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}
time_dict = {
    "ms": 3600 * 1000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "d": 1 / 24,
    "month": 1 / 168,
    "y": 1 / (24 * 365 + 6 + 9 / 60) # accounts for leap years
}
mass_dict= {
    "mg": 1000,
    "g": 1,
    "kg": .001,
    "T": .000001,
}
# combine for checking
all_units = {**distance_dict,**time_dict,**mass_dict}

# unit categories
def get_category(unit):
    if unit in distance_dict:
        return "distance"
    elif unit in time_dict:
        return "time"
    elif unit in mass_dict:
        return "mass"
    else:
        return None
# Get amount and units (assume they are valid)
amount = float(input("how much? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = all_units[from_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = all_units[to_unit]
answer = standard / divide_by
if (from_unit in distance_dict and to_unit in distance_dict or
        from_unit in mass_dict and to_unit in mass_dict or
        from_unit in time_dict and to_unit in time_dict):
    print(f"There are {answer} {to_unit} in {amount} {from_unit}")
    print()

# check if units are valid
if from_unit not in all_units or to_unit not in all_units:
    print(f"Cannot convert, enter a valid answer")
else:
    from_cat = get_category(from_unit)
    to_cat = get_category(to_unit)
    if from_cat != to_cat:
        print(f"Cannot convert {from_unit}({from_cat}) to {to_unit}({to_cat})")
        print()


while True:
    to_convert = num_check("End?: ")
    print("You chose to end, I hope you enjoyed")

    if to_convert == "xxx":
        break

print(f"Thank you for using the ultimate conversion calculator!")