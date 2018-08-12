-- LMPOP key count
local key = KEYS[1]
local count = table.remove(ARGV, 1)
local reply = {}
for _ = 1, count do
    local ele = redis.call('LPOP', key)
    if ele then
        table.insert(reply, ele)
    end
end
return reply
