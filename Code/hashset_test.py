#!python

from hashset import HashSet
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert len(hs.buckets) == 4
        assert hs.size == 0

    def test_init_with_list(self):
        hs = HashSet(['A', 'B', 'C'])
        assert len(hs.buckets) == 6
        assert hs.size == 3

    def test_items(self):
        hs = HashSet()
        assert hs.items() == []
        hs.add('I')
        assert hs.items() == ['I']
        hs.add('V')
        self.assertCountEqual(hs.items(), ['I', 'V'])
        hs.add('X')
        self.assertCountEqual(hs.items(), ['I', 'V', 'X'])

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add('I')
        assert hs.size == 1
        hs.add('V')
        assert hs.size == 2
        hs.add('X')
        assert hs.size == 3

    def test_contains(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.contains('I') is True
        assert hs.contains('V') is True
        assert hs.contains('X') is True
        assert hs.contains('A') is False

    def test_add(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.size == 3
        hs.add('I')
        assert hs.size == 3

    def test_resize(self):
        hs = HashSet(['A', 'B', 'C'])
        assert hs.size == 3
        assert len(hs.buckets) == 6
        assert hs.load_factor() == 0.5
        hs.add('D')
        assert hs.size == 4
        assert len(hs.buckets) == 6
        assert hs.load_factor() == 0.6666666666666666
        hs.add('E')
        assert hs.size == 5
        assert len(hs.buckets) == 12
        assert hs.load_factor() == 0.4166666666666667

    def test_remove(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.size == 3
        hs.remove('I')
        hs.remove('X')
        assert hs.size == 1
        with self.assertRaises(ValueError):
            hs.remove('X')  # Key no longer exists
        with self.assertRaises(ValueError):
            hs.remove('A')  # Key does not exist

    def test_union_with(self):
        hs = HashSet(['A', 'B', 'C'])
        hs2 = HashSet(['D'])
        assert hs.size == 3
        assert hs2.size == 1
        hs3 = hs.union_with(hs2)
        assert hs3.size == 4
        for item in hs.items():
            assert hs3.contains(item)
        for items in hs2.items():
            assert hs3.contains(item)

    def test_intersection_with(self):
        hs = HashSet(['A', 'B', 'C'])
        hs2 = HashSet(['A', 'B'])
        for item in hs.intersection_with(hs2).items():
            assert hs.contains(item) and hs2.contains(item)
        hs3 = HashSet(['D', 'E', 'F'])
        assert hs.intersection_with(hs3).size is 0

    def test_difference_from(self):
        hs = HashSet(['A', 'B', 'C'])
        hs2 = HashSet(['A', 'B'])
        for item in hs.difference_from(hs2).items():
            assert hs2.contains(item) is False
        assert hs.difference_from(hs).size is 0

    def test_is_subset(self):
        hs = HashSet(['I', 'V', 'X'])
        assert hs.size == 3
        assert hs.is_subset(HashSet(['V'])) == True
        assert hs.is_subset(HashSet(['V', 'X'])) == True
        assert hs.is_subset(HashSet(['I', 'V', 'X'])) == True
        assert hs.is_subset(HashSet(['A', 'B', 'C'])) == False
        assert hs.is_subset(HashSet(['I', 'V', 'X', 'Y'])) == False
        assert hs.is_subset(HashSet(['V', 'X', 'Y'])) == False


if __name__ == '__main__':
    unittest.main()
