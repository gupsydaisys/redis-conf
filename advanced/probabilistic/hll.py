import redis
import random
import string


#################################################
#  Some helper functions
#################################################

def rand_str(size):
   r = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(size)])
   return r


#################################################
#  Establish the connection to Redis and test it
#  Test if you can create an item by using the
#  'execute_command' command!
#################################################

# <Your code goes here>

#################################################
#  Generate a list of 10K random string values
#################################################

samples = []

for i in range(0, 10000):
     samples.append(rand_str(20))

#################################################
#  Add the first 5000 and the last 2500 values
#  to the HLL 'hyper'
#################################################

# <Your code goes here>

#################################################
#  Add the last 2500 values to the HLL 'loglog'
#################################################

# <Your code goes here>

#################################################
# Estimate the cardinalities of
#  - 'hyper'
#  - 'loglog'
#  - 'the merge of hyper and loglog'
#################################################

# <Your code goes here>

print('hyper : {}, loglog : {}, merged : {}'.format(c_hyper, c_loglog, c_merged))
