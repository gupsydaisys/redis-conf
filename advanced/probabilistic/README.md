# Probabilistic Data Structures

These exercises are demonstrating the Bloom Filter and HyperLogLog features. Both are provided by probabilistic data structures (as module or as core feature). A probabilistic data structure is used in order to address a specific problem more space efficient than its deterministic counterpart. On the other hands side probabilistic data structures are returning approximated results instead of exact ones. Bloom Filters are used in order to determine if an item is likely to be in a set. The HyperLogLog algorithm addresses the 'count distinct' problem.

This directory contains files to use for the exercise. The bloom.py program provides a skeleton to help you get started with the Bloom Filter exercise. The hll.py script represents the skeleton for the HyperLogLog exercise.

If you get stuck, bloom_solution.py and hll_solution.py are implementing the solutions to the exercises. Feel free to study it or ask questions of the training staff.

Although this is a hands-on exercise, we want to encourage you to use this time to ask questions of the training staff as well!


##  Exercise 1 - Bloom Filters

### Prerequisites

* Use one of the provided Cloud instances OR install a local Redis >= 4.x
* Make sure that the ReBloom module is installed
* Double check that you can access your database by using `redis-cli`
* A source code editor of your choice (e.g. Vim)
* Python >=2.7.x
* Make sure that `redis-py` is installed
* Verify that you can import the `redis` module via Python’s CLI

### Step 1 - Filter Creation

* All steps should be addressed by a single Python script
* Create a bloom filter called ‘bloomy’ with an error rate of 0.1% and an initial capacity of 1000 slots

### Step 2 - Prepare the Dataset

* Prepare a list of 10000 values (e.g. random strings)

### Step 3 - Add to the filter

* Add the first 5000 values of your dataset to the filter

### Step 4 - Check for existing items

* Take 10 samples from the first 5000 values in your dataset and check if they are contained

### Step 5 - Check for non-existent items

* Take 10 samples from the last 5000 values in your dataset and check if they are contained

### Step 6 - Analyze the filter

* Analyze the debug output of your bloom filter

## Exercise 2 - HyperLogLog

### Prerequisites

* Use one of the provided Cloud instances OR install a local Redis >= 4.x
* Double check that you can access your database by using `redis-cli`
* A source code editor of your choice (e.g. Vim)
* Python >=2.7.x
* Make sure that `redis-py` is installed
* Verify that you can import the `redis` module via Python’s CLI

### Step 1 - Two HLL-s

* Write a Python script again
* The first HLL is called ‘hyper’
* The second HLL is called ‘loglog’

### Step 2 - Prepare the Dataset

* Prepare a list of 10000 values (e.g. random strings)

### Step 3 - Add to ‘hyper’

* Add the first 5000 values of your dataset to the HLL ‘hyper’
* Add the last 2500 values of your dataset, too

### Step 4 - Add to ‘loglog’ 

* Add the first 2500 items of your dataset again to the HLL ‘loglog’

### Step 5 - Estimate the cardinalities

Estimate the cardinality of:

* the HLL ‘hyper’
* the HLL ‘loglog’
* the merged HLL-s ‘hyper’ and ‘loglog’






