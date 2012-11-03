# coding=utf-8

import rotx


_letter_pairs = {
    'a': ('b', 'b'),
    'b': ('c', 'c'),
    'x': ('y', 'y'),
    'y': ('z', 'z'),
    'z': ('a', '{'),
    '1': ('1', '2'),
    '&': ('&', '\''),
    '\xe5': ('\xe5', '\xe6'),
}


_letter_offset_pairs = dict((k, v[0]) for k, v in _letter_pairs.items())
_letter_offset_pairs.update({
    '1': None,
    '&': None,
    '\xe5': None,
})


def pytest_generate_tests(metafunc):
    if 'letter_pair' in metafunc.funcargnames:
        metafunc.parametrize('letter_pair', _letter_pairs.items())
    if 'letter_offset_pair' in metafunc.funcargnames:
        metafunc.parametrize('letter_offset_pair', _letter_offset_pairs.items())
    if 'n' in metafunc.funcargnames:
        metafunc.parametrize('n', [1])


def test_get_max_ord():
    assert rotx._get_max_ord(str) == 255

    # No reliable way to check for what the unicode value should be,
    # since it depends on whether the Python build uses UCS2 or UCS4
    assert rotx._get_max_ord(unicode) > 255


def test_rot_letter_offset(letter_offset_pair, n):
    input, expected = letter_offset_pair

    assert rotx._rot_letter_offset(ord(input), n, ord('a'), ord('z')) == (None if expected is None else ord(expected))


def test_rot_letter(letter_pair, n):
    input, (expected_alpha_only, expected_all) = letter_pair

    _chr = rotx._type_chr(type(input))
    assert _chr(rotx._rot_letter(input, n, alphabetical_only=True)) == expected_alpha_only
    assert _chr(rotx._rot_letter(input, n, alphabetical_only=False)) == expected_all


def test_rot(n):
    data_pairs = _letter_pairs.items()
    input = reduce((lambda seed, x: seed + x[0]), data_pairs, '')
    expected_pairs = reduce((lambda seed, x: seed + (x[1],)), data_pairs, ())

    expected_alpha_only, expected_all = ('',) * 2

    for alpha_only, all in expected_pairs:
        expected_alpha_only += alpha_only
        expected_all += all

    assert rotx.rot(input, n, alphabetical_only=True) == expected_alpha_only
    assert rotx.rot(input, n, alphabetical_only=False) == expected_all
