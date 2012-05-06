# The syntax for set literals has been backported from Python 3.x. Curly brackets are used to surround the contents of the resulting mutable set; set literals are distinguished from dictionaries by not containing colons and values. {} continues to represent an empty dictionary; use set() for an empty set.
print type({1, 2, })
print type({})

# Dictionary and set comprehensions are another feature backported from 3.x, generalizing list/generator comprehensions to use the literal syntax for sets and dictionaries.
d = {x: x*x for x in range(6)}
print type(d), d
s = {('a'*x) for x in range(6)}
print type(s), s
