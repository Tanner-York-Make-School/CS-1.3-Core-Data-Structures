#!python

from doublylinkedlist import DoublyLinkedList, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.next is None


class DoublyLinkedListTest(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head == None
        assert dll.tail == None
        assert dll.size == 0

    def test_init_with_list(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.head.data == 'A'
        assert dll.tail.data == 'C'
        assert dll.size == 3

    def test_items(self):
        dll = DoublyLinkedList()
        assert dll.items() == []
        dll.append('B')
        assert dll.items() == ['B']
        dll.prepend('A')
        assert dll.items() == ['A', 'B']
        dll.append('C')
        assert dll.items() == ['A', 'B', 'C']

    def test_length(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        # append and prepend operations increase length
        dll.append('B')
        assert dll.length() == 1
        dll.prepend('A')
        assert dll.length() == 2
        dll.append('C')
        assert dll.length() == 3
        # delete operations decrease length
        dll.delete('B')
        assert dll.length() == 2
        dll.delete('C')
        assert dll.length() == 1
        dll.delete('A')
        assert dll.length() == 0

    def test_size(self):
        dll = DoublyLinkedList()
        assert dll.size == 0
        # append and prepend operations increment size
        dll.append('B')
        assert dll.size == 1
        dll.prepend('A')
        assert dll.size == 2
        dll.append('C')
        assert dll.size == 3
        # delete operations decrement size
        dll.delete('B')
        assert dll.size == 2
        dll.delete('C')
        assert dll.size == 1
        dll.delete('A')
        assert dll.size == 0

    def test_get_at_index(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.get_at_index(0) == 'A'  # head item
        assert dll.get_at_index(1) == 'B'  # middle item
        assert dll.get_at_index(2) == 'C'  # tail item
        with self.assertRaises(ValueError):
            dll.get_at_index(3)  # index too high
        with self.assertRaises(ValueError):
            dll.get_at_index(-1)  # index too low

    def test_insert_at_index(self):
        dll = DoublyLinkedList()
        dll.insert_at_index(0, 'B')  # append('B')
        assert dll.head.data == 'B'  # new head (at index 0)
        assert dll.tail.data == 'B'  # new tail (at index 0)
        assert dll.size == 1
        dll.insert_at_index(0, 'A')  # prepend('A')
        assert dll.head.data == 'A'  # new head (at index 0)
        assert dll.tail.data == 'B'  # unchanged (now at index 1)
        assert dll.size == 2
        dll.insert_at_index(2, 'D')  # append('D')
        assert dll.head.data == 'A'  # unchanged (at index 0)
        assert dll.tail.data == 'D'  # new tail (now at index 2)
        assert dll.size == 3
        dll.insert_at_index(2, 'C')  # insert 'C' between 'B' and 'D'
        assert dll.head.data == 'A'  # unchanged (at index 0)
        assert dll.tail.data == 'D'  # unchanged (now at index 3)
        assert dll.size == 4
        with self.assertRaises(ValueError):
            dll.insert_at_index(5, 'X')  # index too high
        with self.assertRaises(ValueError):
            dll.insert_at_index(-1, 'Y')  # index too low

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append('A')
        assert dll.head.data == 'A'  # new head
        assert dll.tail.data == 'A'  # new tail
        assert dll.size == 1
        dll.append('B')
        assert dll.head.data == 'A'  # unchanged
        assert dll.tail.data == 'B'  # new tail
        assert dll.size == 2
        dll.append('C')
        assert dll.head.data == 'A'  # unchanged
        assert dll.tail.data == 'C'  # new tail
        assert dll.size == 3

    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend('C')
        assert dll.head.data == 'C'  # new head
        assert dll.tail.data == 'C'  # new head
        assert dll.size == 1
        dll.prepend('B')
        assert dll.head.data == 'B'  # new head
        assert dll.tail.data == 'C'  # unchanged
        assert dll.size == 2
        dll.prepend('A')
        assert dll.head.data == 'A'  # new head
        assert dll.tail.data == 'C'  # unchanged
        assert dll.size == 3

    def test_find(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.find(lambda item: item == 'B') == 'B'
        assert dll.find(lambda item: item < 'B') == 'A'
        assert dll.find(lambda item: item > 'B') == 'C'
        assert dll.find(lambda item: item == 'X') is None

    def test_replace(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        dll.replace('A', 'D')
        assert dll.head.data == 'D'  # new head
        assert dll.tail.data == 'C'  # unchanged
        assert dll.size == 3
        dll.replace('B', 'E')
        assert dll.head.data == 'D'  # unchanged
        assert dll.tail.data == 'C'  # unchanged
        assert dll.size == 3
        dll.replace('C', 'F')
        assert dll.head.data == 'D'  # unchanged
        assert dll.tail.data == 'F'  # new tail
        assert dll.size == 3
        with self.assertRaises(ValueError):
            dll.replace('X', 'Y')  # item not in list

    def test_delete(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        dll.delete('A')
        assert dll.head.data == 'B'  # new head
        assert dll.tail.data == 'C'  # unchanged
        assert dll.size == 2
        dll.delete('C')
        assert dll.head.data == 'B'  # unchanged
        assert dll.tail.data == 'B'  # new tail
        assert dll.size == 1
        dll.delete('B')
        assert dll.head is None  # new head
        assert dll.tail is None  # new head
        assert dll.size == 0
        with self.assertRaises(ValueError):
            dll.delete('X')  # item not in list


if __name__ == '__main__':
    unittest.main()
