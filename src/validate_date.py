import re

def validate_date(date_input):
    """
    Date validation rules:
        - Starts with a number (number should be 1-31)
        - Then either of these signs (dot '.'  dash '-' slash '/')
        - Then a number (1-12)
        - Then again either of these signs (dot '.'  dash '-' slash '/')
        - then year from 2000 - 2099

    :param date_input: <str> The string containing date to be checked
    :return: True if date_input respects any of date format. Returns False otherwise
    """
    # Define the regular expression pattern for date validation
    pattern = r'^(0?[1-9]|[12][0-9]|3[01])([.\-/])(0?[1-9]|1[0-2])\2(20[0-9]{2}|2099)$'
    
    # Use the re.match function to check if the input matches the pattern
    if re.match(pattern, date_input):
        return True
    else:
        return False
