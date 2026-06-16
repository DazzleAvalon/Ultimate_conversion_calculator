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

statement_generator("The Ultimate Conversion Calculator" ,"-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions " 
                          "or any key to continue ")

if want_instructions == "":
    instructions()