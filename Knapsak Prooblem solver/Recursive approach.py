# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:04:58 2020

@author: Tanveer Mahmood Hasan
"""


# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity W 
def knapSack(W, wt, val, n): 

	# Base Case 
	if n == 0 or W == 0 : 
		return 0

	# If weight of the nth item is 
	# more than Knapsack of capacity W, 
	# then this item cannot be included 
	# in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
				knapSack(W, wt, val, n-1)) 

# end of function knapSack 

# To test above function 
val = [23,45,25,92,44,65,38,73,94,85,12,36,16,77,66,45,56,99,72,89,91,38,78,45,60,51,0,87,63,88,62,51] 
wt = [6,2,9,8,4,8,3,9,1,9,3,7,4,1,2,8,0,5,5,0,3,3,8,1,2,1,2,5,6,6,2,9]
W = 65
n = 32
print (knapSack(W, wt, val, n) )


