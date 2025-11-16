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
while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
