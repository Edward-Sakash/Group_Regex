import re


def validate_email(email_input):
    """
    Email validation rules:
        - Case insensitive
        - Starts with a letter
        - At least two characters before the @
        - The characters before the @ are letters, digits, underscore '_', dash '-', and dot '.'
        - after the @ the characters accepted are letters, digits, underscore '_', dash '-', and dot '.'
        - after the @ there can't be 2 dots in a row '..'
        - The email address end with a dot followed by 2 to 5 letters. Example ".me", ".com", ".euro" ".rugby"

    :param email_input: <str> The string to be checked
    :return: True if email_input respects the email format. Returns False otherwise
    """
    pass


