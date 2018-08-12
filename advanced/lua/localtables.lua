local empty = {}
local associative = { ['key1'] = 'value1', [42] = true }
associative['newkey'] = { ['another_key'] = { 'table' }, }
local indexed = { 6, 'afraid', 7 }  -- 1-based index! 
indexed[#indexed+1] = 'because'
table.insert(indexed, 7)
table.remove(indexed)
return indexed[4]

