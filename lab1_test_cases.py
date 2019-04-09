import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_val_error(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_maxes(self):
        self.assertEqual(max_list_iter([1,2,3,4,5]), 5)
        self.assertEqual(max_list_iter([2,2,1,1,1]), 2)
        self.assertEqual(max_list_iter([5,1,5,1]), 5)
        self.assertEqual(max_list_iter([5,5,5]), 5)
        self.assertEqual(max_list_iter([1,5,1]), 5)
        self.assertEqual(max_list_iter([5,1,5]), 5)
        self.assertEqual(max_list_iter([5,5,1]), 5)
        


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8]),[8,7,6,5,4,3,2,1])
        self.assertEqual(reverse_rec([1,2,3,2,1]),[1,2,3,2,1])
        self.assertEqual(reverse_rec([1,2]),[2,1])




    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        self.assertEqual(bin_search(0, low, high, list_val), 0 )
        self.assertEqual(bin_search(1, low, high, list_val), 1 )
        self.assertEqual(bin_search(2, low, high, list_val), 2 )
        self.assertEqual(bin_search(3, low, high, list_val), 3 )
        self.assertEqual(bin_search(5, low, high, list_val), None )
        self.assertEqual(bin_search(7, low, high, list_val), 5 )
        self.assertEqual(bin_search(8, low, high, list_val), 6 )
        self.assertEqual(bin_search(9, low, high, list_val), 7 )
        self.assertEqual(bin_search(10, low, high, list_val), 8 )
        self.assertEqual(bin_search(11, low, high, list_val), None )



if __name__ == "__main__":
        unittest.main()

    
