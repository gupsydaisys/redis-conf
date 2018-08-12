import redis

# connect to redis
r = redis.Redis(
    host='yourhost',
    port=6379,
    password='yourpassword')

rediSearchIndex = 'movies'
documentId = 'r999999'
documentScore = 1

readyPlayerOne = {
  'budget'            : 175000000,
  'original_language' : 'en',
  'original_title'    : 'Ready Player One',
  'overview'          : 'When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune.',
  'popularity'        : 10,
  'release_date'      : 1522303200000,
  'revenue'           : 400502798,
  'runtime'           : 140,
  'status'            : 'Released',
  'title'             : 'Ready Player One',
  'vote_average'      : 5.8,
  'vote_count'        : 1292,
  'spoken_languages'  : 'en',
  'keywords'          : 'video game, scifi'
}


addResponse = r.execute_command(
  'FT.ADD',
  #....
)

print(addResponse)
