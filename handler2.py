# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:57:04 2020

@author: kisku
"""

def f2(x):
    b = 0 
    c = 0
    c+= 1
    try:
        if(x==1):
            raise ArithmeticError  # here we can use vustom error to handle this.
    except ArithmeticError:
            print("X must not equal to 1:")
    else:
        b = x + c
    finally:
        print(c)
        return b

print(f2(1))
print(c)
