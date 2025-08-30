calculation_to_minute = 24 * 60
name_of_unit = "minutes"

def days_to_units(num_of_days, custom_result):
    return f"{num_of_days} days are {num_of_days * calculation_to_minute} {name_of_unit}"
    print(custom_result)

days_to_units(20, "awesome !")
