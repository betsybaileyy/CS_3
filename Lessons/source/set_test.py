#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set([1, 2, 3])
        assert test_set.map.length() == 3
        assert test_set.map.contains(3) == True
        assert test_set.map.contains(5) == False

    def test_contains(self):
        test_set = Set([1, 2, 3])
        assert test_set.map.contains(3) == True
        assert test_set.map.contains(5) == False
        assert test_set.map.contains(6) == False
        assert test_set.map.contains(7) == False
        assert test_set.map.contains(1) == True

    def test_add(self):
        test_set = Set([1, 2, 3, 4, 5, 6, 7])
        self.map.add(5)
        self.map.add(3)
        self.map.add(9)
        self.map.add(8)
        assert test_set.map.contains(3) == True
        assert test_set.map.contains(5) == True
        assert test_set.map.contains(9) == False
        assert test_set.map.contains(8) == False

    def test_remove(self):
        test_set = Set([1, 2, 3, 4, 5, 6, 7])
        self.map.remove(5)
        self.map.remove(3)
        assert test_set.map.contains(3) == False
        assert test_set.map.contains(5) == False
        assert test_set.map.contains(9) == False
        assert test_set.map.contains(8) == False



if __name__ == '__main__':
    unittest.main()
