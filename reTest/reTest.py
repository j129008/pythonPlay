# coding: utf-8
import re

s1 = "hello world1, world2, world3"
match = re.search("world.", s1)
print(match.group())
