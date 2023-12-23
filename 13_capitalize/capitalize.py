def capitalize(phrase):
    for first_letter in phrase:
        if first_letter == phrase[0]:
            return phrase.replace(first_letter,first_letter.upper(),1)
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """