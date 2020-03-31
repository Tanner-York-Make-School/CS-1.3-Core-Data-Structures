#!python

import string
BASE_CHARACTERS = set(string.ascii_lowercase)


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def clean_text(text):
    cleaned_text = []
    for char in text:
        if char.lower() in BASE_CHARACTERS:
            cleaned_text.append(char.lower())
    return ''.join(cleaned_text)


def is_palindrome_iterative(text):
    text = clean_text(text)
    left_index, right_index = 0, len(text)-1
    while left_index < right_index:
        if text[left_index] != text[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    text = clean_text(text)
    if left == None and right == None:
        return is_palindrome_recursive(text.lower(), 0, len(text)-1)
    if left > right:
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome_recursive(text, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
