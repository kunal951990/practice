# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:50:04 2020

@author: kisku

8. Implement a simple generator for Fibonacci series
9. Write an iterator class that iterators over a sequence of values in the reverse
direction
10. Implement a decorator that quantifies and returns the execution time of any
function

"""

# Question 8

def fib(limit): 
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x = fib(5) 

for i in x:
    print(i)
    

#  Question 9

class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __iter__(self):
        return self
    
    
    
    
    
    
    
# Question 10

start_time = int(round(time.time() * 1000))
employees = Employee.get_all_employee_details() 
time_diff = current_milli_time() — start_time debug_log_time_diff.update({'FETCH_TIME': time_diff})

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print '%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000)
        return result
    return timed

@timeit
def get_all_employee_details(**kwargs):
    print('employee details')