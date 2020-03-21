# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:02:19 2020

@author: kisku

Implement a child class called mathnew and parent classes as sqroot, addition,
subtraction, multiplication and division. Use the super () function to inherit the
parent methods.

"""
import math

class sqroot(object):
    def sq(self):
        number = int(input("Enter a number:"))
        square_root = 0
        square_root = math.sqrt(number)
        print("Square Root is:",square_root)

class addition(object):
    def add(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x+y)

class subtraction(object):
    def sub(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x-y)

class multiplication(object):
    def mul(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x*y)
        
class division(object):
    def div(self):
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        print(x/y)

class mathnew(sqroot, addition, subtraction, multiplication, division):
    def __init__(self):
        print("\n1. Square Root:")
        print("\n2. Addition:")
        print("\n3. Substraction:")
        print("\n4. Multiplication:")
        print("\n5. Division:")
        user_input=int(input("Enter the operation needs to be performed:"))
        if(user_input==1):
            super().sq()
        if(user_input==2):
            super().add()
        if(user_input==3):
            super().sub()
        if(user_input==4):
            super().mul()
        if(user_input==4):
            super().div()
            
obj = mathnew()