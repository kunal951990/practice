# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:17:41 2020

@author: kisku
"""

import re

"""
a. digit at the beginning of the string and a digit at the end of the string
b. A string that contains only whitespace characters or word characters
c. A string containing no whitespace characters """


# to find digit in begining and end of string.
re.findall(r"(?<!\d)\d+(?!\d)", text)

# to find string that contains only whitespace characters or word characters.
re.findall(r"[\w\s]*",text)

# string containing no whitespace characters
re.findall(r"[^\W]*",text)
