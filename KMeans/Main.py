# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 02:12:44 2023

@author: a
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from IPython.display import clear_output
import matplotlib.pyplot as plt

# Load iris dataset
iris = load_iris()

# Shuffle the data
data, target = iris.data, iris.target
shuffle_idx = np.arange(len(target))

np.random.shuffle(shuffle_idx)
data, target = data[shuffle_idx], target[shuffle_idx]





def newcen(Claster):  
    x1=0
    x2=0
    x3=0
    x4=0
    E11=0        
    for i in range(0,len(Claster)):
        x1+=Claster[i][0]
        x2+=Claster[i][1]
        x3+=Claster[i][2]
        x4+=Claster[i][3]
        
    E11=[x1/4,x2/4,x3/4,x4/4]
    return E11  
        
    






E1=data[0]
E2=data[50]
E3=data[120]
while True:
    
    
  
    Claster1=[]
    Claster2=[]
    Claster3=[]
    newFina=[E1,E2,E3]
    for i in range(0,150):
        arr=[]
        Current_Data = np.array(data[i])
        First_Claster = np.array(newFina[0])
        Second_Claster = np.array(newFina[1])
        Third_Claster = np.array(newFina[2])
        distance1 = np.linalg.norm(Current_Data - First_Claster)
        distance2 = np.linalg.norm(Current_Data - Second_Claster)
        distance3 = np.linalg.norm(Current_Data - Third_Claster)
        arr.append(distance1)
        arr.append(distance2)
        arr.append(distance3)
        Min=min(arr)
        if(Min==distance1):
            Claster1.append(Current_Data)
        elif(Min==distance2):
            Claster2.append(Current_Data)
        else:
            Claster3.append(Current_Data)

    Fina=[Claster1,Claster2,Claster3]
    
    Old=[E1,E2,E3]
    for i in range(0,3):
        newFina.append(newcen(Fina[i]))
        
    n1 = np.array(newFina[0])
    n2 = np.array(newFina[1])
    n3 = np.array(newFina[2])
    o1 = np.array(Old[0])
    o2 = np.array(Old[1])
    o3 = np.array(Old[2])
    distance111 = np.linalg.norm(n1 - o1)
    distance22 = np.linalg.norm(n2 - o2)
    distance33 = np.linalg.norm(n3 - o3)
    cc=distance111+distance22+distance33

    if(cc==0):
        
        print("Equal")
        break;
    
    




print("First Claster")
print(newFina[0])
print("-----------")
for i in range(0,len(Claster1)):
    print(Claster1[i])
    
print("*************")

print("Sconde Claster")
print(newFina[1])
print("-----------")
for i in range(0,len(Claster2)):
    print(Claster2[i])
    
print("*************")

print("Third Claster")    
print(newFina[2])
print("-----------")
for i in range(0,len(Claster3)):
    print(Claster3[i])   
    


print(len(Claster1))
print(len(Claster2))
print(len(Claster3))
