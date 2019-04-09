import unittest
from location import *

class TestLab1(unittest.TestCase):

	def test_repr(self):
		loc = Location("SLO", 35.3, -120.7)
		loc2 = Location("SLO", 35, -120)
		loc3 = Location("Paris", 130, -54)
		loc4 = Location("India", 15.22, 15.22)

		self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)") #test simple location
		self.assertEqual(repr(loc2),"Location('SLO', 35.0, -120.0)") #test whole number lon and lat 
		self.assertEqual(repr(loc3),"Location('Paris', 130.0, -54.0)") #test whole number lon and lat
		self.assertEqual(repr(loc4),"Location('India', 15.2, 15.2)") #test truncated lon and lat


	def test_eq(self):
		loc1 = Location("SLO", 35.3, -120.7)
		loc2 = Location("Paris", 48.9, 2.4)
		loc3 = Location("SLO", 35.3, -120.7)
		loc4 = loc1
		self.assertEqual(loc1,loc3) # two seperate locations are the same
		self.assertEqual(loc1,loc4) # alias locations are the same
		self.assertNotEqual(loc1,loc2) # two seperate locations are not the same



if __name__ == "__main__":
	unittest.main()
