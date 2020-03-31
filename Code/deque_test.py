#!python

from deque import Deque
import unittest

class DequeTest(unittest.TestCase):

    def test_init(self):
        dq = Deque()
        assert dq.length() == 0
        assert dq.is_empty() is True

    def test_init_with_list(self):
        dq = Deque(['A', 'B', 'C'])
        assert dq.length() == 3
        assert dq.is_empty() is False
        assert dq.front() == 'A'
        assert dq.back() == 'C'

    def test_length(self):
        dq = Deque()
        assert dq.length() == 0
        dq.push_front('A')
        assert dq.length() == 1
        dq.push_front('B')
        assert dq.length() == 2
    
    def test_push_front(self):
        dq = Deque()
        dq.push_front('A')
        assert dq.length() == 1
        assert dq.front() == 'A'
        assert dq.back() == 'A'
        dq.push_front('B')
        assert dq.length() == 2
        assert dq.front() == 'B'
        assert dq.back() == 'A'

    def test_push_back(self):
        dq = Deque()
        dq.push_back('A')
        assert dq.length() == 1
        assert dq.front() == 'A'
        assert dq.back() == 'A'
        dq.push_back('B')
        assert dq.length() == 2
        assert dq.front() == 'A'
        assert dq.back() == 'B'

    def test_pop_front(self):
        dq = Deque(['A', 'B', 'C'])
        assert dq.pop_front() == 'A'
        assert dq.pop_front() == 'B'
        assert dq.pop_front() == 'C'
        assert dq.pop_front() == None

    def test_pop_back(self):
        dq = Deque(['A', 'B', 'C'])
        assert dq.pop_back() == 'C'
        assert dq.pop_back() == 'B'
        assert dq.pop_back() == 'A'
        assert dq.pop_back() == None