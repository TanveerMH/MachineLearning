# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:00:05 2020

@author: Hasan Tanveer Mahmood 1725413


"""

import time

startTime = time.time()

values = [23,45,25,92,44,65,38,73,94,85,12,36,16,77,66,45,56,99,72,89,91,38,78,45,60,51,0,87,63,88,62,51] 
weights = [6,2,9,8,4,8,3,9,10,9,3,7,4,1,2,8,0,5,5,0,3,3,8,1,2,1,2,5,6,6,2,9]
totalItem = len(values)
maxWeight = 65
accuracy = 0
excutionTime = 0
expectedOptimal = 1313

mat = [[0 for i in range(maxWeight + 1)] for i in range(totalItem + 1)] 



#Main logic
'''for item in range(1,totalItem+1):
    for capacity in range(1,maxWeight+1):
        currentMaxValue = 0
        if capacity >= weights[item-1]:
            currWeight = weights[item-1]
            currentMaxValue = values[item-1] + mat[item-1][capacity-currWeight]
        mat[item][capacity] = max(mat[item-1][capacity] , currentMaxValue)
    print(mat)
'''
    
for item in range(1,totalItem+1):
    for capacity in range(1,maxWeight+1):
        maxValWithoutCurr = mat[item - 1][capacity]
        maxValWithCurr = 0
        weightOfCurr = weights[item - 1]
        if capacity >= weightOfCurr:
            maxValWithCurr = values[item - 1]
            remainingCapacity = capacity - weightOfCurr
            maxValWithCurr += mat[item - 1][remainingCapacity]
            
        if maxValWithoutCurr > maxValWithCurr:
            mat[item][capacity] = maxValWithoutCurr
        else :
            mat[item][capacity] = maxValWithCurr
 
endTime =time.time()
excutionTime = endTime - startTime
print("\nThe execution Time : %.3f" % excutionTime +" sec")       
accuracy = mat[totalItem][maxWeight]/expectedOptimal * 100
print("Accuracy : ",accuracy ,"%")
print("The optimal Value is: ", mat[totalItem][maxWeight])

'''for x in mat:
    print(x)'''