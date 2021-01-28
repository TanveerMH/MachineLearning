# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:42:56 2020

@author: Hasan Tanveer Mahmood, Matric no:1725413
"""
import random
import csv

#column names
fields = ['Fever', 'DryCoughLevel','TriednessLevel', 'sortanceOfBreath','BloodPressure','Label']

# 1 = Corona , 2 = Normal Sickness , 3 = Pneumonia
#Fever level 97 to 99.1 Fahrenheit is normal 
# DryCough Level 1 to 10, 10 is higher
# TriednessLevel Lavel 1 to 4 is normal
# sortanceOfBreath Lavel 12 to 20 is normal
# BloodPressure Lavel 12 to 20 mm Hg is normal 

#define syntomps Level for Corona
def Corona ():
    Fever = round(random.uniform(104 , 105),2)
    DryCoughLavel = random.randint(8,10)
    TriednessLavel = random.randint(8,10)
    sortanceOfBreath = random.randint(5,10)
    BloodPressure = round(random.uniform(121,139),2)
    
    return Fever,DryCoughLavel,TriednessLavel,sortanceOfBreath,BloodPressure,1

#define syntomps Level for NormalSickness
def NormalSickness ():
    Fever = round(random.uniform(97 , 100),2)
    DryCoughLavel = random.randint(1,3)
    TriednessLavel = random.randint(1,4)
    sortanceOfBreath = random.randint(12,20)
    BloodPressure = round(random.uniform(80,120),2)
    
    return Fever,DryCoughLavel,TriednessLavel,sortanceOfBreath,BloodPressure,2

#define syntomps Level for Pneumonia
def Pneumonia ():
    Fever = round(random.uniform(101 , 103),2)
    DryCoughLavel = random.randint(4,7)
    TriednessLavel = random.randint(5,7)
    sortanceOfBreath = random.randint(6,11)
    BloodPressure = round(random.uniform(59,79),2)
    
    return Fever,DryCoughLavel,TriednessLavel,sortanceOfBreath,BloodPressure,3
 
data = []

#declare, how many data will generate for each section
TotalNum = 500

#create a loop for new object of each diseases
while TotalNum > 0:
    #create an object for Corona
    newCorona = Corona()
    data.append(newCorona)
    
    #create an object for normal sickness
    newNormalSickness = NormalSickness()
    data.append(newNormalSickness)
    
    #create an object for pneumonia 
    newPneumonia = Pneumonia()
    data.append(newPneumonia)
    
    TotalNum -=1

#here create a file and declare the location where it will save 
filename = "F:\SEM 04\INTELEGENCE SYSTEM\QUIZE 2\Quize 2\diseases.csv"

with open(filename,'w',newline ='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(fields)
    
    for eachdata in data:
        csvwriter.writerow(eachdata)
    
    
    