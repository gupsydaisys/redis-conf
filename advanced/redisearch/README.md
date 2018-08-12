# Exercises for RediSearch during RedisConf Day0 Training

# Install

Run:

```
$ pip3 install -r requirements.txt
```

This should install `redis-py`

You will need RediSearch installed.

# Populating

This script relies on having a pre-populated data set from the TMDB 5000. There is a node.js script that will do this for you from a CSV file. During the training this should be prepopulated.


# Running

There are three Python files which are stubs for you to fill out:

  * `schema.py` - building a schema exercise
  * `add.py` - adding an item exercise
  * `query.py` - query syntax expercise

These files can be executed with `python3`