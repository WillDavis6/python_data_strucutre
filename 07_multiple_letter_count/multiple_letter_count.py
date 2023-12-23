def multiple_letter_count(phrase):
    sett = {letter for letter in phrase}
    number = 0
    obj = {letter: number for letter in sett}
    for letter in phrase:
        if letter in obj:
            obj[letter] += 1
    return obj
    
    
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """