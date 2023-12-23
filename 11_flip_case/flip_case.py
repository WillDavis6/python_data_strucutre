def flip_case(phrase, to_swap):
    phrase_list = list(phrase)
    for letter in phrase_list:
        if letter.upper() == to_swap:
            print(phrase_list(letter))
            letter.lower()
        elif letter.lower() == to_swap:
            letter.upper()
        else:
            letter
    return "".join(phrase_list)

        
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
