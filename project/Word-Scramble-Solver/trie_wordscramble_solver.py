#!python

import anagram_trie
from anagram_trie import AnagramTrie, AnagramTrieNode


class WordScrambleSolver():
    """A class for solving word scambles using an anagram trie"""

    def __init__(self, path_to_anagram_trie):
        """Initalize this words scample solver"""
        self.anagram_trie = anagram_trie.load_from_file(path_to_anagram_trie)

    def unscramble(self, text=None, letters=None):
        """Retuns a list of the given text's anagrams"""
        if text is not None:
            return self.anagram_trie.find_anagrams(sorted(text))
        if letters is not None:
            unscambled_words = []
            for text in letters:
                sorted_text = self.unscramble(sorted(text))
                unscambled_words.append(sorted_text)
            return unscambled_words


if __name__ == '__main__':
    scramble_solver = WordScrambleSolver('usrs_trie_solver.pkl')
    print(scramble_solver.unscramble(letters=['dgo', 'eevasl']))
