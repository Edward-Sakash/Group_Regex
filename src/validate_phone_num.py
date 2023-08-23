import re

def validate_phone_num(phone_num_input):
    """
    It will validate the phone number
    rules:
            - starts with + symbol
            - then country code (number in range 1-999)
            - then space
            - then (
            - then area code (1 - 999)
            - then space
            - then three digits
            - then space
            - then 4 digits

    :param input: <str> The string input
    :return: True if phone number is valid else False
    """
    # Define the regular expression pattern for phone number validation
    pattern = r'^\+\d{1,3}\s\(\d{1,3}\)\s\d{3}\s\d{4}$'
    
    # Use the re.match function to check if the input matches the pattern
    if re.match(pattern, phone_num_input):
        return True
    else:
        return False
