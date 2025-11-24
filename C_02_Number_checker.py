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

# Main routine goes here
for item in range(0, 2):
    number = num_check("Number: ")
    print(number)
