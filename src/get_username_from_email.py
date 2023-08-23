import re

def get_username_from_email(email):
    """
    It would extract the first part of the email (the part before @ symbol)

    :param email: <str> The string input
    :return: <str> The before @ part of the email
    """
    # Use regular expression to match the username part before the @ symbol
    match = re.match(r'^\w+', email)
    
    if match:
        return match.group()  # Return the matched username
    else:
        return None  # Return None if no match is found
