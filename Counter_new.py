#!/usr/bin/env python2.7

#see http://bugs.python.org/issue1696199

#the Counter class in the collections module is useful for tallying data. 
#Counter instances behave mostly like dictionaries but return zero for missing keys instead of raising a KeyError

from collections import Counter

counter = Counter()

for letter in 'what is new in python2.7':
    counter[letter] += 1
print counter
#Counter({' ': 4, 'n': 3, 'i': 2, 'h': 2, 't': 2, 'w': 2, 'a': 1, 'e': 1, '7': 1, 'o': 1, 'p': 1, 's': 1, '2': 1, 'y': 1, '.': 1})

print counter['n']
#3
print counter['m']
#0

#Three additional methods for Counter
#1. most_common(n=None)
#List the n most common elements and their counts from the most common to the least.
#If n is None, then list all element counts.

print counter.most_common(3)
#[(' ', 4), ('n', 3), ('i', 2)]

#2. elements()
#return iterator over elements repeating each as many times as its count
print sorted(counter.elements())
#[' ', ' ', ' ', ' ', '.', '2', '7', 'a', 'e', 'h', 'h', 'i', 'i', 'n', 'n', 'n', 'o', 'p', 's', 't', 't', 'w', 'w', 'y']

#3. subtract(source=None, **kwds)
#Like dict.update() but subtracts counts instead of replacing them.
#Counts can be reduced below zero.  Both the inputs and outputs are allowed to contain zero and negative counts.
#Source can be an iterable, a dictionary, or another Counter instance

c = Counter('which')
c.subtract('witch')
print c
#Counter({'h': 1, 'i': 0, 'c': 0, 'w': 0, 't': -1})
c.subtract(Counter('watch'))
print c
#Counter({'i': 0, 'h': 0, 'a': -1, 'c': -1, 'w': -1, 't': -2})
print c['h']
#0
print c['w']
#-1

