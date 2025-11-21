# Generates headings (eg: ---- Heading ---- )
def statement_generator(statement, decoration):
        print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
        statement_generator("Instructions", "-")

        print('''
      Instructions
      1) give a calc_type (time,mass,distance)
      2) give the amount / quantity  of the calc_type
      3) gve the unit you would like to change from
      4) give the unit you would like to change this to
      5) if you want to keep using the program enter another calc_type but if you want to finish code type xxx
        ''')


# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "please enter a number that is more than zero\n"
    while True:

        try:
            #ask the user for a number
            response = float(input(question))

        # check that the number is more than zero
            if response > 0:
                return response

            else :  print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
statement_generator("The ultimate Conversion Calculator", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions"
                          "or any key to continue")

if want_instructions == "":
    instructions()

# define domains
valid_type = ["time", "mass" , "distance"]

# Set up dictionaries
time_dict = {
    "ms":3600000 ,
    "s": 3600,
    "min":60,
    "h": 1,
    "d": 1/24,
    "m":1/168,
    "y": 1 / (24 * 365 + 6 + 9/60)  # it accounts for leap years
}

mass_dict = {
    "mg": 1000,
    "g": 1,
    "kg": .001,
    "t": .000001,
}

distance_dict = {
    "mm" : 1000,
    "cm" :100,
    "m" : 1 ,
    "km" :0.001
}

while True:
    calc_type = input("calc_type: ").strip().lower()
    if calc_type == "xxx":
        print("Thank you using conversion calculator!!!^-^")
        break
    if calc_type not in valid_type:
        print("Please enter a valid calculation type.")
        continue

    # Get amount and units (assume they are valid)
    amount = float(input("how much?"))
    from_unit = input("from unit?")
    to_unit = input("To Unit?")

    #set up loop
    if calc_type == "time":
        dictionary = time_dict

    elif calc_type == "mass":
        dictionary = mass_dict

    else:
        dictionary = distance_dict

    # Multiply to get our standard value...
    multiply_by = dictionary[to_unit]
    print(multiply_by)
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = dictionary[from_unit]
    answer = standard / divide_by

    # Look up value
    # multiply_by = distance_dict[to_unit]
    # answer = amount * multiply_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit}")


