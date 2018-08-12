-- ZSUMRANGE key start stop
local total = 0
local data = redis.call('ZRANGE', KEYS[1], ARGV[1], ARGV[2], 'WITHSCORES')
while #data > 0 do
    -- ZRANGE replies with an array in which scores are at even indices
    total = total + tonumber(table.remove(data))
    table.remove(data)
end
return total 