# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:27:35 2020

@author: kisku
"""

import time

i=1
try:
    while(i<5):
        time.sleep(1)
        print(i)
        i+=1
except KeyboardInterrupt:
    print("KeyboardInterrupt")
else:
    print("This is else part.")
finally:
    print("Executing Finally...")
       
try:
    name = input("Enter your name:")
    print("Good Morning "+ name)
except NameError:#Enter your name in Quotes else NameError msg will appear
    print("NameError")



try:
    num = 0/0
except ArithmeticError:
    print("ArithmeticError")
        

print('End of program')