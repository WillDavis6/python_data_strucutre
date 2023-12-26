def flip_case(phrase, to_swap):
    lower_to_swap = to_swap.lower()
    new_phrase = []
    for letter in phrase:
        if letter.lower() == lower_to_swap:
            if letter == lower_to_swap:
                new_phrase.append(letter.upper())
            elif letter != lower_to_swap:
                new_phrase.append(letter.lower())
        else:
            new_phrase.append(letter)
    return ''.join(new_phrase)
            
        

        
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
