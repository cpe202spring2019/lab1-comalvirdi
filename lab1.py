# Comal Virdi
# CPE 202



from math import *


# this function finds the max of a list of numbers and returns the value (not the index)
#If int_list is empty, returns None. If list is None, raises ValueError 
# list --> int
def max_list_iter(int_list):  	
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return None
	max_temp = float('-inf')
	for x in int_list:
		if x > max_temp:
			max_temp = x
		elif x == max_temp:
			max_temp = x
	return max_temp



"""recursively reverses a list of numbers and returns the reversed list
	If list is None, raises ValueError"""
# list --> list
def reverse_rec(int_list):   # must use recursion
	
	if int_list == None:
		raise ValueError
	if len(int_list)==1:
		return int_list
	return reverse_rec(int_list[1:]) + [int_list[0]]
	


"""searches for target in int_list[low..high] and returns index if found
	If target is not found returns None. If list is None, raises ValueError """
	# int int int list --> int
def bin_search(target, low, high, int_list):  
	
	if int_list == None:
		raise ValueError
	if high < low:
		return None
	mid = (high+low)//2
	if int_list[mid] == target:
		return mid
	if int_list[mid] > target:
		high = mid - 1
	if int_list[mid] < target:
		low = mid + 1 
	return bin_search(target, low, high, int_list)


