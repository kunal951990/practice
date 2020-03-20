# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:15:01 2020

@author: kisku
"""

import math

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

def find_log(n):
    print(math.log10(n))
    
def radian(n):
    print(math.radians(n)) 

def to_get_sin_cos_tan(n):
    print("\nsin(n)",math.sin(n))
    print("\ncos(n)",math.cos(n))
    print("\ntan(n)",math.tan(n))

    
a=1
while(a==1):
    print("\n1. Factorial:")
    print("\n2. log10:")
    print("\n3. Radian:")
    print("\n4. Get sin,cos,tan:")
    choice=int(input("Enter your choice:"))
    if choice==1:
        n=int(input("Enter your number:"))
        factorial(n)
    if choice==2:
        n=int(input("Enter your number for getting log:"))
        find_log(n)
    if choice==3:
        n=int(input("Enter the degree which needs to be converted into radian: "))
        radian(n)
    if choice==4:
        n=int(input("Enter the degree to get trignometric ratios:"))
        to_get_sin_cos_tan(n)
    if choice==5:
        break