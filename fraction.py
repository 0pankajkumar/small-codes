#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    positive = 0
    negative = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
     
    a = positive / n
    b = negative / n
    c = zero / n
    print "a"
    #

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
