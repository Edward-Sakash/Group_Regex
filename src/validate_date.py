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
    pass

