#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Best Case Runtime: O(k) where k is the length of the pattern and the fist
        patter is found at the fist index
    Worst Case Runtime: O(n*k) where n is the size fo the text and k is the
        size of the pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pattern_start, index, count = 0, 0, 0
    while count != len(pattern) and index != len(text):
        if text[index] == pattern[count]:
            pattern_start = index if count == 0 else pattern_start
            count += 1
        else: 
            index -= count if count != 0 else 0
            count = 0
        index += 1
    return True if count == len(pattern) else False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Best Case Runtime: O(k) where k is the length of the pattern and the fist
        patter is found at the fist index
    Worst Case Runtime: O(n*k) where n is the size fo the text and k is the
        size of the pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if text == '' or text == ' ':
         return None
    pattern_start, index, count = 0, 0, 0
    while count != len(pattern) and index != len(text):
        if text[index] == pattern[count]:
            pattern_start = index if count == 0 else pattern_start
            count += 1
        else: 
            index -= count if count != 0 else 0
            count = 0
        index += 1
    return pattern_start if count == len(pattern) else None
    
    #The code below does not account for edge case that looks for a 
    #pattern that has the same character in a row and does not follow DRY
    # index, count = 0, 0
    # for i in range(0, len(text)):
    #     if text[i] == pattern[count]:
    #         if count == 0: 
    #             index = i
    #         count += 1
    #     else:
    #         count = 0
    #         if text[i] == pattern[count]:
    #             if count == 0: 
    #                 index = i
    #             count += 1
    #     if count == len(pattern):
    #         return index
    #return False
        

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Best and Worst Case Runtime: O(n*k) where n is the lenght of the text  and k 
        is the length of the pattern becuase the algorythm goes through the entire 
        text minus k no matter the size of the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return [index for index in range(0, len(text))]
    pattern_start, index, count, indexes = 0, 0, 0, []
    while index != len(text):
        start_index = index
        if index+len(pattern) <= len(text):
            for char in pattern:
                if text[index] != char: break
                pattern_start = index if index == start_index else pattern_start
                index += 1
                if index-start_index == len(pattern): 
                    indexes.append(pattern_start)
                    break
        index = start_index
        index += 1
    return indexes

    #The code below does not account for patters starting 
    #inside the pattern itself (aa in aaa)
    #     if text[index] == pattern[count]:
    #         pattern_start = index if count == 0 else pattern_start
    #         count += 1
    #     else: 
    #         index -= count if count != 0 else 0
    #         count = 0
    #     if count == len(pattern):
    #         indexes.append(pattern_start)
    #         count, pattern_start = 0, 0
    #     index += 1
    # return indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))

def find_index_test():
    print(find_index('bananas', 'nas'))
    print(find_index('bannns', 'nns'))

def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
