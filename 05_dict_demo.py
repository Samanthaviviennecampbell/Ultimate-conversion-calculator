distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001,
}

# Get amount and units (assume they are valid)
amount = float(input("how much?"))
from_unit = input("from unit?")
to_unit = input("To Unit?")

# Multiply to get our standard value...
multiply_by = distance_dict[to_unit]
print(multiply_by)
standard = amount * multiply_by
print(f"there are {standard} m in {from_unit}")

# Divide to get to our desired value
divide_by = distance_dict[from_unit]
answer = standard / divide_by

# Look up value
# multiply_by = distance_dict[to_unit]
# answer = amount * multiply_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")
