# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:02:19 2020

@author: kisku
"""
import math

class sqroot:
    def _init_(self):
        number = int(input("Enter a number:"))
        square_root = 0
        square_root = math.sqrt(number)
        print("Square Root is:",number)

class addition:
    def _init_(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x+y)

class subtraction:
    def _init_(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x-y)

class multiplication:
    def _init_(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x*y)
        
class division:
    def _init_(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x/y)

class mathnew(sqroot, addition, subtraction, multiplication, division):
    def _init_(self):
        super.__init__()