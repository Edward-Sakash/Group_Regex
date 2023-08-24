import re

def format_bio(bio_input):
    """
    Formats the input bio according to specific rules:
    * If it starts with a letter, it must be an uppercase.
    * If there are consecutive multiple spaces, they must be reduced to one space.
    * Each sentence must start with a capital letter, but the case of the rest of the sentence mustn't be modified.
    * After the dot '.' marking the end of a sentence, there must be a space before the following sentence.
    * If there are multiple dots '.' in a row, they mustn't be changed.
    * Remove the trailing spaces in the beginning and the end of the bio.

    :param bio_input: The input bio to be formatted
    :return: A formatted bio respecting the conditions above
    """
    # Remove trailing spaces at the beginning and end of the bio
    bio_input = bio_input.strip()
    
    # Capitalize the first letter if it's a letter
    if bio_input and bio_input[0].isalpha():
        bio_input = bio_input[0].upper() + bio_input[1:]
    
    # Reduce consecutive multiple spaces to one space
    bio_input = re.sub(r'\s+', ' ', bio_input)
    
    # Use regex to find sentences and capitalize the first letter of the first word in each sentence
    sentence_endings = r'(?<=[.!?])\s+'  # Regex to match sentence endings with possible following spaces
    sentences = re.split(sentence_endings, bio_input)
    formatted_sentences = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    
    # Join the sentences and add spaces after dots
    formatted_bio = ' '.join(formatted_sentences)
    formatted_bio = re.sub(r'\.(\w)', r'. \1', formatted_bio)
    
    # Add a dot at the end of the bio
    if formatted_bio and formatted_bio[-1] != '.':
        formatted_bio += '.'
    
    return formatted_bio
