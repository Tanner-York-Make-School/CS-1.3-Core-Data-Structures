#!python


def upload_from_file(name, path_to_file):
    """Creates an anagram dict pickle file from a dictionary file"""
    with open(path_to_file, 'r') as file:
        words = file.read().split('\n')
        anagram_dict = AnagramDict(words=words)
    with open('{}.txt'.format(name), 'w') as dict_file:
        for key in anagram_dict.keys():
            words = ','.join(anagram_dict[key])
            dict_file.write(f'{key}:{words}\n')


def load_from_file(path_to_file):
    """Loads an anagram dict from an anagram tire pickle file"""
    with open(path_to_file, 'r') as dict_file:
        key_values = dict_file.read().split('\n')
        keys_values = []
        for key_value in key_values:
            key_value = key_value.split(':')
            if len(key_value) > 1:
                key, words = key_value[0], key_value[1].split(',')
                keys_values.append((key, words))
        return AnagramDict(key_values=keys_values)


class AnagramDict(dict):

    def __init__(self, words=None, key_values=None):
        """Initializes this anagram dict with the given dicationary or 
            a list of existing key, value pairs from a save AnagramDict"""
        if words is not None:
            for word in words:
                self._add(word)
        elif key_values is not None:
            for key, value in key_values:
                self[key] = value

    def _add(self, word):
        sorted_word = ''.join(sorted(word))
        if sorted_word not in self:
            self[sorted_word] = [word]
        else:
            self[sorted_word].append(word)

    def find_anagrams_of(self, text):
        """Returns the set of anagrams of the given text, if they exist"""
        sorted_text = ''.join(sorted(text))
        return self[sorted_text] if sorted_text in self else None


if __name__ == '__main__':
    upload_from_file('usrs_dict_solver', '/usr/share/dict/words')
