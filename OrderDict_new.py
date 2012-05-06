#!/usr/bin/env python2.7

# PEP 372 - Adding an ordered dictionary to collections
# http://www.python.org/dev/peps/pep-0372

# The OrderedDict API provides the same interface as regular dictionaries but iterates over keys and values in a guaranteed order depending on when a key was first inserted:
from collections import OrderedDict
d = OrderedDict([
        ('first', 1),
        ('second', 2),
        ('third', 3)])
print d.items()

# If a new entry overwrites an existing entry, the original insertion position is left unchanged:
d['second'] = 4
print d.items()

# Deleting an entry and reinserting it will move it to the end:
del d['second']
d['second'] = 5
print d.items()

# The popitem() method has an optional last argument that defaults to True. If last is True, the most recently added key is returned and removed; if it's False, the oldest key is selected:
od = OrderedDict([(x,0) for x in range(10)])
od.popitem()
print od
od.popitem()
print od
od.popitem(last=False)
print od
od.popitem(last=False)
print od

# Comparing two ordered dictionaries checks both the keys and values, and requires that the insertion order was the same:
od1 = OrderedDict([
        ('first', 1),
        ('second', 2),
        ('third', 3)])
od2 = OrderedDict([
        ('third', 3),
        ('first', 1),
        ('second', 2)])
print od1 == od2

# Move 'third' key to the end
del od2['third']; od2['third'] = 3
print od1 == od2

# Comparing an OrderedDict with a regular dictionary ignores the insertion order and just compares the keys and values.
d3 = {'first':1, 'third':3, 'second':2 }
print d3
print od1 == d3

# How does the OrderedDict work? It maintains a doubly-linked list of keys, appending new keys to the list as they're inserted. A secondary dictionary maps keys to their corresponding list node, so deletion doesn't have to traverse the entire linked list and therefore remains O(1).

# The standard library now supports use of ordered dictionaries in several modules.
# - The ConfigParser module uses them by default, meaning that configuration files can now be read, modified, and then written back in their original order.
conf = '''
[auth]
allow = foo, bar'''
import tempfile
fn = tempfile.mktemp()
f = open(fn, 'w')
f.write(conf)
f.close()

from ConfigParser import ConfigParser
cp = ConfigParser()
cp.read(fn)
print cp._dict

import os
os.remove(fn)

# - The _asdict() method for collections.namedtuple() now returns an ordered dictionary with the values appearing in the same order as the underlying tuple indices.
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(11, y = 22)
print p._asdict()

# - The json module's JSONDecoder class constructor was extended with an object_pairs_hook parameter to allow OrderedDict instances to be built by the decoder. Support was also added for third-party tools like PyYAML.

# - From http://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict-in-python
from json import JSONDecoder
s = '{"first":1, "second":2, "third":3}'
print s
print eval(s)
print JSONDecoder(object_pairs_hook=OrderedDict).decode(s)
