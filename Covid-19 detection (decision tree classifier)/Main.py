# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:30:59 2020

@author: Hasan Tanveer Mahmood, Matric no:1725413
"""

import csv
from sklearn import tree
data = []

filename = "F:\SEM 04\INTELEGENCE SYSTEM\QUIZE 2\diseases.csv"

#read the file
with open(filename) as csvDataFile:
    
    csvReader = csv.reader(csvDataFile)
    
    for row in csvReader:
        data.append(row)
        
csvDataFile.close
data.pop(0)
features = []
labels = []

for records in data:
    features.append([records[0],records[1],records[2],records[3],records[4]])
    labels.append(records[5])
    
    
trainfeat = []
trainlabl = []

testfeat = []
testlabl = []

stopindex = 1099
while stopindex >= 0:
    trainfeat.append(features[stopindex])
    trainlabl.append(labels[stopindex])
    stopindex -= 1
    
startindex = 1100
while startindex <= 1499:
    testfeat.append(features[startindex])
    testlabl.append(labels[startindex])
    startindex += 1
    
clsfr = tree.DecisionTreeClassifier()
clsfr = clsfr.fit(trainfeat,trainlabl)

prediction = clsfr.predict(testfeat)

#show the accuracy
accuracy = len(set(testlabl)&set(prediction)) / float(len(set(testlabl) | set(prediction))) * 100
print ("\nThe accuracy of our model is "+ str(accuracy) +" %")
