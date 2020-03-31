#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return False if self.list.head else True

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) beacuase adding an item to the 
            front of a linked list is just changing pointers
            which takes O(1) time"""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        return self.list.head.data if self.list.head else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because removing a item form the front 
            of a linked list is just changing pointers which 
            takes O(1) time"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.list.head.data
        self.list.delete(item)
        return item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return True if len(self.list) == 0 else False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) because appending to a list 
        (dynamic array) is setting a pointer to a new value
        (exept when we need to find more space for array) which
        takes O(1) time"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        return self.list[len(self.list)-1] if len(self.list) > 0 else None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because the built in list pop method
        removes the last item in the list and since python list
        are dynamic and indexing is O(1) it takes O(1) time to
        remove the last item"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
