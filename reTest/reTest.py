# coding: utf-8
import re

s1 = "hello world1, world2, world3"
p = re.compile("world\d")
print (p.findall(s1))
