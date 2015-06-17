# coding: utf-8
# %load reTest.py
import re

s1 = "hello world"
s2 = "world"
match = re.search(s2, s1)
print(match.group())
