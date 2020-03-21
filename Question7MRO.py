# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:15:02 2020

@author: kisku

Create a class called First and two classes called Second and Third which inherit
from First. Create class called Fourth which inherits from Second and Third.
Create a common method called method1 in all the classes and provide the
Method Resolution Order

"""

class First(object):
    def display(self):
        print("Class First:")

class Second(First):
    def display(self):
        print("Class Second:")

class Third(First):
    def display(self):
        print("Class Third:")

class Fourth(Second,Third):
    def display(self):
        print("Class Fourth:")
        
obj_Fourth = Fourth()
obj_Fourth.display()

# here the MRO will be Fourth , Second , Third , First

