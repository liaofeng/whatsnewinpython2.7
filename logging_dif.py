# Python 2.7 adds a dictConfig() function that uses a dictionary to configure logging. There are many ways to produce a dictionary from different sources: construct one with code; parse a file containing JSON; or use a YAML parsing library if one is installed. For more information see Configuration functions.

import logging
import logging.config

from tempfile import mktemp
fn = mktemp()

configdict = {
    'version': 1,    # Configuration schema in use; must be 1 for now
    'formatters': {
        'standard': {
            'format': ('%(asctime)s %(name)-15s ' '%(levelname)-8s %(message)s')
        }
    },
    'handlers': {
        'netlog': {
            'backupCount': 10,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': fn,
            'formatter': 'standard',
            'level': 'INFO',
            'maxBytes': 1000000
        },
    },
    # Specify all the subordinate loggers
    'loggers': { 'network': { 'handlers': ['netlog'] } }, 
    # Specify properties of the root logger 
    'root': { 'handlers': ['netlog'] },
}

# Set up configuration
logging.config.dictConfig(configdict)

# As an example, log two error messages
logger = logging.getLogger('/')
logger.error('Socket timeout')

netlogger = logging.getLogger('network')
netlogger.error('Connection refused')

print 'Content read from fn:\n'
import sys, os
sys.stdout.write(open(fn).read())
os.remove(fn)
