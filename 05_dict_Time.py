time_dict = {
    "ms":3600000 ,
    "s": 3600,
    "min":60,
    "h": 1,
    "d": 1/24,
    "m":1/168,
    "y": 1 / (24 * 365 + 6 + 9/60)  # it accounts for leap years
}

# Get amount and units (assume they are valid)
amount = float(input("how much?"))
from_unit = input("from unit?")
to_unit = input("To Unit?")

# Multiply to get our standard value...
multiply_by = time_dict[to_unit]
print(multiply_by)
standard = amount * multiply_by
print(f"there are {standard} m in {from_unit}")

# Divide to get to our desired value
divide_by = time_dict[from_unit]
answer = standard / divide_by

# Look up value
# multiply_by = distance_dict[to_unit]
# answer = amount * multiply_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")
