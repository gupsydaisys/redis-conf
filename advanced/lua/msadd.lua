-- MSADD key1 key2 ele
local set1, set2 = KEYS[1], KEYS[2]
local rep1 = redis.call('SADD', set1, unpack(ARGV))
local rep2 = redis.call('SADD', set2, unpack(ARGV))
return rep1 + rep2