try:  # Detect whether the Python build uses UCS-4 or UCS-2, used to determine when to wrap around
    unichr(0x10FFFF)
    _py_ucs4 = True
except ValueError:
    _py_ucs4 = False


def _get_max_ord(type):
    "The max ordinal that should be used for a given type"
    if issubclass(type, unicode):
        return 0x10FFFF if _py_ucs4 else 0xFFFF
    else:
        return 255


def _type_chr(type):
    "The reverse of ord() to use for a given type"
    return unichr if issubclass(type, unicode) else chr


def _rot_letter_offset(ordinal, n, offset, max):
    """Does the actual rotation for a single ordinal

    :param ordinal: The original value to rotate
    :param n: The amount to rotate by
    :param offset: The offset to start from
    :param max: The maximum value (anything above this is wrapped around)
    :returns: The rotated value if offset <= ordinal <= max, otherwise None
    """
    if offset <= ordinal <= max:
        ordinal -= offset
        ordinal += n
        ordinal %= max - offset + 1
        ordinal += offset
        return ordinal


def _rot_letter(ordinal, n, alphabetical_only):
    """Rotates a single ordinal semi-intelligently, based on it's type

    :param ordinal: The original value to rotate
    :param n: The amount to rotate by
    :param alphabetical_only: Whether to rotate in the full space of possible values, or just rotate a-Z (like a caesar cipher)
    """
    assert isinstance(ordinal, int) or isinstance(ordinal, long)

    if alphabetical_only:
        result_ord = _rot_letter_offset(ordinal, n, 97, 122)  # Lower-case
        if result_ord:
            return result_ord

        result_ord = _rot_letter_offset(ordinal, n, 65, 90)  # Upper-case
        if result_ord:
            return result_ord

        return ordinal
    else:
        return _rot_letter_offset(ordinal, n, 0, _get_max_ord(type(input)))


def rot(input, n, alphabetical_only=True):
    """Rotates all the characters in a string

    :param input: The input string
    :param n: The amount to rotate by
    :param alphabetical_only: :param alphabetical_only: Whether to rotate in the full space of possible values, or just rotate a-Z (like a caesar cipher)
    """
    _type = type(input)
    _chr = _type_chr(_type)
    return _type().join(_chr(_rot_letter(ord(i), n, alphabetical_only)) for i in input)
