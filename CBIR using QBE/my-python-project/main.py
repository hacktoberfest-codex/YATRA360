calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else: return "You entered wrong input"


user_input = int(input("Enter Number of Days \n"))  

print(days_to_units(user_input))