#!python

import pickle


def upload_from_file(name, path_to_file):
    """Creates an anagram trie pickle file from a dictionary file"""
    with open(path_to_file, 'r') as file:
        words = file.read().split('\n')
        anagram_trie = AnagramTrie(name, words)
    with open('{}_anagram_trie.pkl'.format(name), 'wb') as pkl:
        pickle.dump(anagram_trie, pkl, pickle.HIGHEST_PROTOCOL)


def load_from_file(path_to_file):
    """Loads an anagram trie from an anagram tire pickle file"""
    with open(path_to_file, 'rb') as anagram_tree:
        return pickle.load(anagram_tree)


class AnagramTrieNode(object):
    """"An object meant to make a list of dictionary words into a 
        trie where the words are sorrtted before put into the tree"""

    def __init__(self, data=None):
        """Initialize this anagram tree node with the given data."""
        self.data = data
        self.children = {}  # think about advateges/disadvateges of changing to an array
        self.anagrams = set()


class AnagramTrie(object):

    def __init__(self, name, dicationary):
        """Initializes this anagram tree with the given dicationary"""
        self.name = name
        self.root = AnagramTrieNode()
        self._generate_anagram_trie(dicationary)

    def _generate_anagram_trie(self, dicationary):
        """Generates an anagram tree from a list of words from a dictionary"""
        for word in dicationary:
            self._append_to_trie(word)

    def _append_to_trie(self, word):
        """Add the given word to the trie"""
        node = self.root
        for letter in sorted(word):
            new_node = AnagramTrieNode(letter)
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = new_node
                node = new_node
        node.anagrams.add(word)

    def find_anagrams(self, text):
        """Returns the set of anagrams of the given text, if they exist"""
        node = self.root
        for letter in text:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return node.anagrams


if __name__ == '__main__':
    upload_from_file('usr', '/usr/share/dict/words')
