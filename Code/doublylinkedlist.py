#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.prev = None
        self.next = None
    
    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize the linked list and append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' <-> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Returns all the items in the doubly linked list"""
        result = []
        node = self.head
        while node is not None:
            result.append(node.data)
            node = node.next
        return result

    def is_empty(self):
        """Returns True is list is empty and False if not"""
        return True if self.head is None else False

    def length(self):
        """Returns the lenght(size) if the list"""
        return self.size

    def get_at_index(self, index):
        """Returns the item at the index or rases a value error if
        index exceeds the size of the list"""
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node.data

    def insert_at_index(self, index, item):
        """Inserts an item into the list at a given index or rases a
        value error is index is greater that the size of the list or 
        less that 0"""
        node = self.head
        new_node = Node(item)
        
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        
        if self.size > 0:
            while index > 1:
                node = node.next
                index -= 1
            
            if node.prev is not None:
                if node.next is None: 
                    self.tail = new_node
                node.prev.next = new_node
                new_node.prev = node.prev
            if node.prev is None:
                self.head = new_node
            new_node.next = node
            node.prev = new_node
        else:
            self.head, self.tail = new_node, new_node
        self.size += 1

    def append(self, item):
        """Intert a given item at the end of the list"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert a given item at the beging of the list"""
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item based on the quality or None if no item was
        found with the quality"""
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def replace(self, old_item, new_item):
        """Replaces the node's data that holds the old data with the new data
        or None if there is no node that holds old data"""
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                break
            node = node.next
        else: raise ValueError('Item not found in list')

    def delete(self, item):
        """Delete the given item from the list, or raise a value error"""
        node = self.head
        found = False
        while not found and node is not None:
            if node.data == item:
                found = True
            else:
                node = node.next

            if found:
                if node is not self.head and node is not self.tail:
                    if node.next is not None:
                        node.next.prev = node.prev
                    node.prev.next = node.next
                    node.prev = None
                    node.next = None
                if node is self.head:
                    if self.head is not None:
                        self.head.prev = None
                    self.head = node.next
                    node.next = None
                if node is self.tail:
                    self.tail = node.prev
                    if node.prev is not None:
                        node.prev.next = None
                        node.prev = None
                self.size -= 1
                break
        else:
            raise ValueError('Item not found: {}'.format(item))


def test_doubly_linked_list():
    ll = DoublyLinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()


    



            