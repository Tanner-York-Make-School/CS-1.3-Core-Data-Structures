#!python

from linkedlist import LinkedList


class HashSet(object):

    def __init__(self, data=None):
        """Initialize this set with the given data"""
        init_size = len(data)*2 if data is not None else 4
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0
        if data is not None:
            for item in data:
                self.add(item)

    def __str__(self):
        """Return a formatted string representation of this set"""
        items = ['{!r}'.format(item) for item in self.items()]
        return '(' + ', '.join(items) + ')'

    def __repr__(self):
        """Return a string representation of this set"""
        return "Set({!r})".format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored.
            Best and worst case running time: O(1)"""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
            Best and worst case running time: O(1)"""
        return self.size/len(self.buckets)

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
            Best and worst case running time: O(n)"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def contains(self, item):
        """Returns a booling indicating whether an item is in this set.
            Best case running time: O(1)
            Worst case running time: O(l) where l is items/buckets"""
        index = self._bucket_index(item)
        bucket = self.buckets[index]
        if bucket.find(lambda value: value == item):
            return True
        return False

    def add(self, item):
        """Adds element to set, if item is not already in set.
            Best case running time: O(1)
            Worst case running time: O(l) where l is items/buckets"""
        index = self._bucket_index(item)
        bucket = self.buckets[index]
        if self.contains(item) is False:
            bucket.append(item)
            self.size += 1
        if self.load_factor() > 0.75:
            self._resize()

    def remove(self, item):
        """Removed item from set or rasises value error if item is not in set
            Best case running time: O(1)
            Worst case running time: O(l) where l is items/buckets"""
        if self.contains(item) is False:
            raise ValueError('{} not found in set'.format(item))
        index = self._bucket_index(item)
        bucket = self.buckets[index]
        bucket.delete(item)
        self.size -= 1

    def union_with(self, other_set):
        """Returns the union set of this set and the given set. 
            Best and worst case run time: O(m) where m is the 
            total items in the current and other set"""
        union = HashSet(self.items())
        for item in other_set.items():
            if self.contains(item) is False:
                union.add(item)
        return union

    def intersection_with(self, other_set):
        """Returns the intersection set of this set and the given set
            Best and worst case run time: O(min(n, m))"""
        intersection = HashSet()
        smaller = self if self.size <= other_set.size else other_set
        larger = other_set if self.size >= other_set.size else self

        for item in smaller.items():
            if larger.contains(item):
                intersection.add(item)
        return intersection

    def difference_from(self, other_set):
        """Returns the difference set of this set and the given set
            Best and worst case run time: O(min(n, m))"""
        difference = HashSet()
        smaller = self if self.size <= other_set.size else other_set
        larger = other_set if self.size >= other_set.size else self

        for item in smaller.items():
            if larger.contains(item) is False:
                difference.add(item)
        return difference

    def is_subset(self, other_set):
        """Returns a booling for if the given set is a subset of the current set
            Best case running time: O(1)
            Worst case running time: O(min(n, m))"""
        if other_set.size > self.size:
            return False
        if self.difference_from(other_set).size is 0:
            return True
        return False

    def _resize(self, new_size=None):
        """Resize this sets hashtable table's buckets and rehash all key-value entries.
            Should be called automatically when load factor exceeds a threshold
            such as 0.75 after an insertion (when set is called with a new key).
            Best and worst case running time: O(n)"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        items = self.items()
        self.size = 0
        self.buckets = [LinkedList() for i in range(new_size)]
        for item in items:
            self.add(item)
