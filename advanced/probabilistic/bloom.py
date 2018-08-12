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
#  Initialize a bloom filter with an error 
#  rate of 0.1% and an initial capacity 
#  of 1000 slots
#################################################

# <Your code goes here>

#################################################
#  Generate a list of 10K random string values
#################################################

samples = []

for i in range(0, 10000):
     samples.append(rand_str(20))

#################################################
#  Add the first 5000 values to the filter
#################################################

# <Your code goes here>

#################################################
#  Take 10 samples from the first 5000 values 
# in the list and check if they are contained
#################################################

# <Your code goes here>

#################################################
#  Take 10 samples from the last 5000 values 
#  in the list and check if they are contained
#################################################

# <Your code goes here>

#################################################
#  Analyze the debug output of your bloom filter
#################################################

# <Your code goes here>
