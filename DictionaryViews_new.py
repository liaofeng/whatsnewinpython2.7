#!/usr/bin/env python2.7

#see: PEP 3106: Revamping dict.keys(), .values() and .items()
#http://www.python.org/dev/peps/pep-3106

#dict.viewkeys() returns the keys of the dict, which can't be modifed.
#Also dict.viewvalues() and dict.viewitems()

d = dict(one=1, two=2, three=3)
print d
print d.viewkeys()

#Views can be iterated over, but the key and item views also behave 'like' (not equal) sets.
#For example: the & operator performs intersection, and | perform a union:

#the type of viewkeys()/viewvalues()/viewitems()

print type(d.viewkeys())
#get '<type 'dict_keys'>'
print type(d.viewvalues())
#get '<type 'dict_values'>'
print type(d.viewitems())
#get '<type 'dict_items'>'

#the result of dict.viewvalues() is not a strict set
d1 = dict(one=1, two=2, three=3, th=3)
print d1.viewvalues()
# get 'dict_values([2, 3, 3, 1])', not dict_values([2, 3, 1]) 

#The view keeps track of the dictionary and its contents change as the dictionary is modified:
vk = d1.viewkeys()
print vk
#get dict_keys(['two', 'three', 'th', 'one'])
d1['four'] = 4
print vk
#get dict_keys(['four', 'two', 'three', 'th', 'one'])

#However, note that you cannot add or remove keys while you'r iterating over the vie
#for k in vk:
#   d[k*2] = k
#get RuntimeError: dictionary changed size during iteration
