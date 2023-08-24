import re

def validate_password(pwd_input):
    """
    At least 8 characters
    At most 30 characters
    At least one Uppercase
    At least one lowercase
    At least one digit
    At least one special character *, !, -, _, .
    Only accept the characters mentioned above

    :param pwd_input:
    :return: True if the pwd_input respect the pattern, False otherwise
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[*!\-_.]).{8,30}$'
    
    if re.match(pattern, pwd_input):
        return True
    else:
        print("Password requirements not met. Please ensure your password follows the rules.")
        return False
