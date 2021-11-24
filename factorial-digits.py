# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:05:19 2021

@author: MEET-PC
"""

import sys
import numpy as np

##get parameter to compute factorial sum and validate
try:
    num=int(sys.argv[1])
except (ValueError,IndexError):
    print("Please provide a positive integer argument.")
    sys.exit()
if (num<0):
    print("Please provide a positive integer argument.")
    sys.exit()
factorial_vec = np.array([1])

##loop through values from 1 to the number computing the multiplication 
##one number at a time
for x in range(1,num+1): 
    left_over = 0
    ## compute the multiplication one digit at a time and save to factorial_vec
    for y in range(len(factorial_vec)):
        mult = left_over + (factorial_vec[y]*x)
        factorial_vec[y] = mult % 10 
        left_over = mult // 10
    ## add additional digits if the multiplication result does not fit in the 
    ## existing digits
    while (left_over!=0):
        factorial_vec = np.append(factorial_vec,left_over % 10) 
        left_over = left_over // 10
sum_of_digits = np.sum(factorial_vec)
print(sum_of_digits)
