class Keymap:
    def __init__(self, chars):
        self.strings = chars
        self.len = len(chars)

    def next(self, count):
        if self.len == 0:
            return self.strings

        charset = []
        while self.len < count:
            charset.append(self.strings[self.len-1])
            count -= self.len
        else:
            charset.append(self.strings[count-1])

        return ''.join(charset)


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    if not keys:
        return ''

    length = len(keys)
    result, index = [], 0
    while index < length:
        key, count = keys[index], index + 1
        while count < length and keys[count] == key:
            count += 1

        keystrokes = keypad[int(key)].next(count - index)
        result.append(keystrokes)
        index = count

    return ''.join(result)


keypad = [
    Keymap(' '),
    Keymap(''),
    Keymap('abc'),
    Keymap('def'),
    Keymap('ghi'),
    Keymap('jkl'),
    Keymap('mno'),
    Keymap('pqrs'),
    Keymap('tuv'),
    Keymap('wxyz'),
]
