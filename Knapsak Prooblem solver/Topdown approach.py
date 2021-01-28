# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:11:31 2020

@author: Tanveer Mahmood Hasan
"""


# driver code 
val = [23,45,25,92,44,65,38,73,94,85,12,36,16,77,66,45,56,99,72,89,91,38,78,45,60,51,0,87,63,88,62,51] 
wt = [6,2,9,8,4,8,3,9,1,9,3,7,4,1,2,8,0,5,5,0,3,3,8,1,2,1,2,5,6,6,2,9]
W = 65
n = 32
  
# We initialize the matrix with -1 at first. 
t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
  
  
def knapsack(wt, val, W, n):     
  
    # base conditions 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
  
    # choice diagram code 
    if wt[n-1] <= W: 
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapsack(wt, val, W, n-1) 
        return t[n][W] 
  
print(knapsack(wt, val, W, n)) 