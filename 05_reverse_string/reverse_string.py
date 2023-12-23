def reverse_string(phrase):
    letters = list(phrase)
    letters.reverse()
    reversed = ''.join(letters)
    return reversed
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
