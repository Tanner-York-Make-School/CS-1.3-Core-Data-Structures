#!python

from linkedlist import LinkedList

class LinkedDeque(object):
    def __init__(self, iterable=None):
        """Initialize this deque and enqueue items, if any."""
        self.list = LinkedList()   
        if iterable is not None:
            for item in iterable:
                self.push_back(item)
    
    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Deque({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return False if self.list.head else True

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size
    
    def push_front(self, item):
        """Prepend given item before the deque list's head
        Time Complexity: O(1) becuase adding to the start of 
            a linked list is simply changing pointers which
            takes O(1) time per operation"""
        self.list.prepend(item)

    def push_back(self, item):
        """Append given item to the end of the deque
        Time Complexity: O(1) becuase adding to the end of 
            a linked list is simply changing pointers which
            takes O(1) time per operation"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list.head.data if self.list.head else None

    def back(self):
        """Return the item at the back of this deque without removing it,
        or None if this queue is empty."""
        return self.list.tail.data if self.list.tail else None

    def pop_front(self):
        """Pop the first item in the deque or None
        Time Complexity: O(1) because removing the first item
            in a linked list is just changing pointers which takes
            O(1) for each change"""
        if self.length() == 0:
            return None
        data = self.list.head.data
        self.list.delete(data)
        return data

    def pop_back(self):
        """Pop the last item in the deque or None
        Time Complexity: O(n) because removing the last item
            in a linked list involes traversing the entire
            list each time and chaning the pointers"""
        if self.length() == 0:
            return None
        data = self.list.tail.data
        self.list.delete(data)
        return data


class ArrayDeque(object):
    def __init__(self, iterable=None):
        """Initialize this deque and enqueue items, if any."""
        self.list = list()   
        if iterable is not None:
            for item in iterable:
                self.push_back(item)
    
    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return True if len(self.list) == 0 else False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)
    
    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list[0] if len(self.list) > 0 else None

    def back(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        return self.list[len(self.list)-1] if len(self.list) > 0 else None

    def push_front(self, item):
        """Prepend given item before the deque list's head
        Time Complexity: O(n) becuase adding to the start of 
            a dynamic list requires you to shift all the other values
            to the right by 1"""
        self.list.insert_at(0, item)

    def push_back(self, item):
        """Append given item to the end of the deque
        Time Complexity: O(1) on average becuase adding to the end of 
            a dynamic list is just adding the the set memory for the list
            but can be O(n) if the set memeory is reached"""
        self.list.append(item)

    def pop_front(self):
        """Pop the first item in the deque or None
        Time Complexity: O(n) becuase removing from the start of 
            a dynamic list requires you to shift all the other values
            to the left by 1"""
        if self.length() == 0:
            return None
        data = self.list[len(self.list)-1]
        self.list.remove(data)
        return data

    def pop_back(self):
        """Pop the last item in the deque or None
        Time Complexity: O(1) because removing the last item
            in a dynamic list involes just removing the item
            at the last index which doesn't require you to 
            shift the other values"""
        if self.length() == 0:
            return None
        data = self.list[len(self.list)-1]
        self.list.remove(data)
        return data

Deque = LinkedDeque
# Deque = ArrayDeque