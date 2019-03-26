#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    temp = 0
    mini = 0
    maxi = 0
    #Sorting in ascending order
    for i in range(0,5):
        for j in range(0,4-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
            
    
    for k in range(0,4):
        mini = mini + arr[k]
    for k in range(1,5):
        maxi = maxi + arr[k]
    
    print mini, maxi
    
    
    
    
    
    
    
if __name__ == '__main__':
    arr = [1,2,3,4,5]

    miniMaxSum(arr)
