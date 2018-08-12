import redis

# connect to redis
r = redis.Redis(
    post='yourhost',
    port=6379,
    password='yourpassword')

rediSearchIndex = 'movies'


queryResponse = r.execute_command(
  'FT.SEARCH',
  rediSearchIndex,
  # query
  #....
)

print(queryResponse)
