#!/usr/bin/env python2.7

#set literal, set/dictionary comprehension are features of python3.1 that were backported to python2.7

#set literal, get a mutable set:
s = {1, 2, 3}
print s
#set([1, 2, 3])
print type(s)
#<type 'set'>

#set comprehension:
s1 = {i*2 for i in range(3)}
print s1
#set([0, 2, 4])

#dictionary comprehension:
d = {i: i*2 for i in range(3)}
print d
#{0: 0, 1: 2, 2: 4}

