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
#  Initialize a bloom filter with an error 
#  rate of 0.1% and an initial capacity 
#  of 1000 slots
#################################################

r.execute_command("BF.RESERVE", "bloomy", 0.001, 1000)

#################################################
#  Generate a list of 10K random string values
#################################################

# <Your code goes here>

samples = []

for i in range(0, 10000):
     samples.append(rand_str(20))

#################################################
#  Add the first 5000 values to the filter
#################################################

# <Your code goes here>

# Side note: In practice, BF.MADD would be better
for i in range(0, 5000):
     r.execute_command("BF.ADD", "bloomy", samples[i])  


#################################################
#  Take 10 samples from the first 5000 values 
# in the list and check if they are contained
#################################################

# <Your code goes here>

for i in range(0, 10):
     exists = r.execute_command("BF.EXISTS", "bloomy", samples[i])
     print('{} : {}'.format(samples[i], exists))

#################################################
#  Take 10 samples from the last 5000 values 
#  in the list and check if they are contained
#################################################

# <Your code goes here>

for i in range(6000, 6010):
     exists = r.execute_command("BF.EXISTS", "bloomy", samples[i])
     print('{} : {}'.format(samples[i], exists))

#################################################
#  Analyze the debug output of your bloom filter
#################################################

# <Your code goes here>

d_out = r.execute_command("BF.DEBUG",  "bloomy")

print(d_out)