def get_season(month, day):
    """
    Determines the season based on the month and day.
    
    :param month: Month as an integer (1 to 12)
    :param day: Day as an integer (1 to 31)
    :return: Name of the season (str)
    """
    if (month == 3 and day >= 21) or (4 <= month <= 6 and not (month == 6 and day > 20)):
        return "Spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 9 and not (month == 9 and day > 22)):
        return "Summer"
    elif (month == 9 and day >= 23) or (10 <= month <= 12 and not (month == 12 and day > 20)):
        return "Autumn (Fall)"
    else:
        return "Winter"

# Get user input
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

# Determine and print the season
season = get_season(month, day)
print(f"The season on {month}/{day} is: {season}")
