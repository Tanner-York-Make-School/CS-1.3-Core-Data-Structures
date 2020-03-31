#!python

import anagram_dict
from anagram_dict import AnagramDict


class DictWordScrambleSolver(object):

    def __init__(self, path_to_file):
        """Initialize this scamble solver with the given list of words"""
        self.anagram_dict = anagram_dict.load_from_file(path_to_file)

    def unscramble(self, text=None, letters=None):
        """Unscabmle a given text or list of scambled text"""
        if text is not None:
            self.anagram_dict.find_anagrams_of(text)
        if letters is not None:
            solved_words = []
            for text in letters:
                sorted_text = self.anagram_dict.find_anagrams_of(text)
                solved_words.append(sorted_text)
            return solved_words


if __name__ == '__main__':
    scramble_solver = DictWordScrambleSolver('usrs_dict_solver.txt')
    print(scramble_solver.unscramble(letters=['dgo', 'eevasl']))
