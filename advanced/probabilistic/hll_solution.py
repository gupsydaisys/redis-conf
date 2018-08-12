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

r = redis.Redis(host='localhost', port=6379, db=0)
r.set("test", "connection=established")
r.execute_command("SET", "test", "connection=established, test=passed")
r.get("test")

#################################################
#  Generate a list of 10K random string values
#################################################

# <Your code goes here>

samples = []

for i in range(0, 10000):
     samples.append(rand_str(20))

#################################################
#  Add the first 5000 and the last 2500 values
#  to the HLL 'hyper'
#################################################

# <Your code goes here>

for i in range(0, 5000):
     r.pfadd("hyper", samples[i])  

for i in range(7500, 10000):
     r.pfadd("hyper", samples[i])

#################################################
#  Add the last 2500 values to the HLL 'loglog'
#################################################

# <Your code goes here>

for i in range(7500, 10000):
     r.pfadd("loglog", samples[i])


#################################################
# Estimate the cardinalities of
#  - 'hyper'
#  - 'loglog'
#  - 'the merge of hyper and loglog'
#################################################

# <Your code goes here>

# Expected: approx. 7500
c_hyper = r.pfcount("hyper")

# Expected: approx. 2500
c_loglog = r.pfcount("loglog")

# Expected: approx. 7500
c_merged = r.pfcount("hyper", "loglog")

print('hyper : {}, loglog : {}, merged : {}'.format(c_hyper, c_loglog, c_merged))