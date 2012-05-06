# PEP 3137: The memoryview Object
# refer to http://docs.python.org/whatsnew/2.7.html#pep-3137-the-memoryview-object

# The memoryview object provides a view of another object's memory content that matches the bytes type's interface.
import string
m = memoryview(string.letters)
print m
print len(m)
print m[0], m[25], m[26]

# The content of the view can be converted to a string of bytes or a list of integers:
m2 = m[0:26]
print m2
print len(m2)
print m2.tobytes()
print m2.tolist()

# memoryview objects allow modifying the underlying object if it's a mutable object.
try:
    m2[0] = 75
except:
    import traceback
    traceback.print_exc()

b = bytearray(string.letters) # Creating a mutable object
print b
mb = memoryview(b)
print mb
mb[0] = '*'     # Assign to view, changing the bytearray.
print mb
print b[0:5]    # The bytearray has been changed.
