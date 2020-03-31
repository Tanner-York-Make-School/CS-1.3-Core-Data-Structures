#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return False if self.list.head else True

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we're using a linked list
            to create the stack we have access to the tail node
            of the queue allowing us to simple set pointers to
            the new node which take O(1) time"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        return self.list.head.data if self.list.head else None

    def dequeue(self):
        """Remove and return the item at the front of self queue,
        or raise ValueError if self queue is empty.
        Running time: O(1) because when removing the head of a
            linked list you're just changin pointers, which takes
            O(1) time complexity per operation"""
        if self.is_empty():
            raise ValueError('No items in queue')
        item = self.list.head.data
        self.list.delete(self.list.head.data)
        return item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return True if len(self.list) == 0 else False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) because we are using a dynamic
        list that knowns its indexs which means it can add
        items at the end in O(1) time """
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        return self.list[0] if len(self.list) > 0 else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) because list are sequentially stored in
        memory so we have to move all the items in the list down one
        after remove the first index"""
        if self.is_empty():
            raise ValueError('No items in queue')
        item = self.list[0]
        del self.list[0]
        return item


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
