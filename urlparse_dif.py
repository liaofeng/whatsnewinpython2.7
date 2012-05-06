# Python 2.7 actually produces slightly different output, since it returns a named tuple instead of a standard tuple.
# The urlparse module also supports IPv6 literal addresses as defined by RFC 2732 (contributed by Senthil Kumaran; issue 2987).
import urlparse
print urlparse.urlsplit('invented://host/filename?query')
