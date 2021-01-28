# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:16:48 2020

@author: Tanveer Mahmood Hasan
"""


def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# Driver program to test above function 
val = [23,45,25,92,44,65,38,73,94,85,12,36,16,77,66,45,56,99,72,89,91,38,78,45,60,51,0,87,63,88,62,51] 
wt = [6,2,9,8,4,8,3,9,1,9,3,7,4,1,2,8,0,5,5,0,3,3,8,1,2,1,2,5,6,6,2,9]
W = 65
n = len(val) 
print(knapSack(W, wt, val, n)) 