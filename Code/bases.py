#!python
import string

# Thanks to @kevin-meyers for reminding me that dictionary comprehension exist
BASE_ENCODE = '0123456789abcdefghijklmnopqrstuvwxyz'
BASE_DECODE = {digit:index for index, digit in enumerate(BASE_ENCODE)}

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    decoded = 0
    for index, digit in enumerate(reversed(digits)):
        decoded += BASE_DECODE[digit] * (base**index)
    return decoded

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    assert type(number) == int
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    
    # Setup conversion variables
    inital_numb = number

    # Divied the number by the base, adding the remainder
    # to converted number, untill number equals 0
    converted_numb = []
    while number > 0:
        div, mod = divmod(number, base)
        number = div
        converted_numb.append(BASE_ENCODE[mod])
    converted_numb.append(BASE_ENCODE[int(number % base)])

    # Pull the important base number digits from the base number
    result = []
    startFound = False
    for digit in reversed(converted_numb):
        if BASE_ENCODE.index(digit) > 0 or startFound:
            startFound = True
            result.append(digit)
    # Add the last digit for the converted number not added from the division
    return ''.join(result)

# Thanks to @tempor1s (Ben) for the recusive version of encode
def recursive_encode(number, base):
    if (number < base):
        return BASE_ENCODE[number]
    div, mod = divmod(number, base)
    return recursive_encode(div, base) + BASE_ENCODE[mod].upper()

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    if base1 == 10: return encode(int(digits), base2)
    return encode(decode(digits, base1), base2)


def test():
    """Test the various functions above"""
    print('____Decode____')
    print(decode('100', 2))
    print(decode('100', 16))
    print(decode('100', 17))

    print('____Encode____')
    print(encode(100, 2))
    print(encode(100, 16))
    print(encode(23423, 17))

    print('____Convert____')
    print(convert('5B7F', 16, 2))

    print(recursive_encode(100, 2))

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    #test()