local sum1 = 0
for i = 1, #ARGV, 1 do
    sum1 = sum1 + tonumber(ARGV[i])
end

local sum2 = 0
for i, v in pairs(ARGV) do
    sum2 = sum2 + tonumber(v)
end

if sum1 ~= sum2 then
    return redis.error_reply('Something meh here')
end

return redis.status_reply('All good \\o/')