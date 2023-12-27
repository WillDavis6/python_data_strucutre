def vowel_count(phrase):
    phrase.lower()
    new_dict = {}
    for letter in phrase:
        if letter not in new_dict:
            if letter in 'aeiou':
                new_dict[letter] = phrase.count(letter)
    return new_dict

    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """