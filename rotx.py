try:
    unichr(0x10FFFF)
    _py_ucs4 = True
except ValueError:
    _py_ucs4 = False


def _get_max_ord(type):
    if issubclass(type, unicode):
        return 0x10FFFF if _py_ucs4 else 0xFFFF
    else:
        return 255


def _type_chr(type):
    return unichr if issubclass(type, unicode) else chr


def _rot_letter_offset(ordinal, n, offset, max):
    if offset <= ordinal <= max:
        ordinal -= offset
        ordinal += n
        ordinal %= max - offset + 1
        ordinal += offset
        return ordinal


def _rot_letter(ordinal, n, alphabetical_only):
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
    _type = type(input)
    _chr = _type_chr(_type)
    return _type().join(_chr(_rot_letter(ord(i), n, alphabetical_only)) for i in input)
