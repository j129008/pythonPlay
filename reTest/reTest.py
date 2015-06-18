# coding: utf-8
import re

s1 = "hello world1, world2, world3"
p = re.compile("(world\d)..(world\d)..(world\d)")
print (p.search(s1).group(2))
