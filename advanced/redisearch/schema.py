import redis

# connect to redis
r = redis.Redis(
    host='yourhost',
    port=6379,
    password='yourpassword')

rediSearchIndex = 'mymovies'

# drop the index so you don't get errors over and over
r.execute_command('FT.DROP', rediSearchIndex)

createResponse = r.execute_command(
    'FT.CREATE',
        rediSearchIndex,
    'SCHEMA',
        #add original_title
        #add revenue
        'budget', 'NUMERIC', 'SORTABLE' 
        'original_language', 'TEXT', 'NOSTEM', 'SORTABLE',
        'overview', 'TEXT',
        'popularity','NUMERIC',
        'release_date','NUMERIC','SORTABLE',
        'runtime','NUMERIC','SORTABLE', 
        'status','TEXT','NOSTEM','SORTABLE', 
        'title','TEXT','WEIGHT','5','SORTABLE', 
        'vote_average','NUMERIC','SORTABLE', 
        'vote_count','NUMERIC','SORTABLE', 
        'spoken_languages','TAG',
        'keywords','TAG')

print(createResponse)