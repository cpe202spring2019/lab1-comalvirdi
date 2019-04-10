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
        self.assertEqual(max_list_iter([1,2,3,4,5]), 5) # tests basic max function
        self.assertEqual(max_list_iter([2,2,1,1,1]), 2) # tests with multiple same min and max vals
        self.assertEqual(max_list_iter([1,2,5,1,2]), 5) # tests with max in middle
        self.assertEqual(max_list_iter([5,5,5]), 5) # tests when list elements are all one number
        self.assertEqual(max_list_iter([1,5,1]), 5) # max is in the middle
        self.assertEqual(max_list_iter([5,1,1]), 5) # max at beginnging
        self.assertEqual(max_list_iter([1,2,5]), 5) # Max at end
        self.assertEqual(max_list_iter([]), None) # Max at end
        


    def test_reverse_rec_val_error(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # simple reversal
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8]),[8,7,6,5,4,3,2,1]) # longer reversal
        self.assertEqual(reverse_rec([1,2,3,2,1]),[1,2,3,2,1]) # reversal is same as original
        self.assertEqual(reverse_rec([1,2]),[2,1]) # simple reversal with two numbers

    

    def test_bin_search_val_error(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 2, 3,tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1

        self.assertEqual(bin_search(0, low, high, list_val), 0 ) # tests target at beginning
        self.assertEqual(bin_search(1, low, high, list_val), 1 ) # tests target in pos 1
        self.assertEqual(bin_search(2, low, high, list_val), 2 ) # tests target in pos 2
        self.assertEqual(bin_search(3, low, high, list_val), 3 ) # tests target in pos 3
        self.assertEqual(bin_search(4, low, high, list_val), 4 ) # tests target in middle
        self.assertEqual(bin_search(7, low, high, list_val), 5 ) # tests target in pos 5
        self.assertEqual(bin_search(8, low, high, list_val), 6 ) # tests target in pos 6
        self.assertEqual(bin_search(9, low, high, list_val), 7 ) # tests target in pos 7
        self.assertEqual(bin_search(10, low, high, list_val), 8 ) # tests target at the end

        self.assertEqual(bin_search(11, low, high, list_val), None ) # tests target not in list
        self.assertEqual(bin_search(5, low, high, list_val), None ) # tests target not in list



if __name__ == "__main__":
        unittest.main()

    
