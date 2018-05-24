from unittest import TestCase

from chapter01.binary_search import binary_search


class TestBinarySearch(TestCase):
    def test_binary_search(self):
        num_list = [1, 3, 5, 6, 7]
        print(binary_search(num_list, 3))
        print(binary_search(num_list, 4))
        print(binary_search(num_list, 5))
