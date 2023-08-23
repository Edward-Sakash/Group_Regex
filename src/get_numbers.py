import re

def get_numbers(input):
    """
    It would take all the numbers that are in the string

    :param input: <str> The string input
    :return: List containing all the numbers that appeared in the string
    """
    # Use regular expression to find all numbers in the input string
    numbers = re.findall(r'\d+', input)
    
    # Convert the found numbers from strings to integers
    numbers = [int(num) for num in numbers]
    
    return numbers
