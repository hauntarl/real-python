import collections
import time
import concurrent.futures
import os

from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])
scientists = (
    Scientist(name='Ada Lovelace', field='math', born='1815', nobel=False),
    Scientist(name='Emmy Noether', field='math', born='1882', nobel=False),
    Scientist(name='Marie Curiee', field='physics', born='1867', nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born='1930', nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born='1939', nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born='1928', nobel=False),
    Scientist(name='Sally Ride', field='physics', born='1951', nobel=False),
)


def transform(x):
    print(f'Process {os.getpid()} is working on {x.name}...')
    time.sleep(1)
    result = {'name': x.name, 'age': 2020 - int(x.born)}
    print(f'Process {os.getpid()} finished processing {x.name}.')
    return result


if __name__ == '__main__':
    start = time.monotonic()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # returns an iterator for efficiency purposes
        result = executor.map(transform, scientists)
    end = time.monotonic()
    print(f'\nProcessor based parallel finished in {end - start:.2f}s.')
    pprint(tuple(result))

print()
if __name__ == '__main__':
    start = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # returns an iterator for efficiency purposes
        result = executor.map(transform, scientists)
    end = time.monotonic()
    print(f'\nThread based parallel finished in {end - start:.2f}s.')
    pprint(tuple(result))

"""
What's going on?
- The process based execution will by default spawn as many processes as number
  of CPU cores, but in Thread based execution, we are only utilizing a single
  process but within that we are creating multiple threads to do our work.

What is the difference between ProcessPoolExecutor() and ThreadPoolExecutor()?
- I'll let you in on Python's dark secret, GIL - Global Interpreter Lock.
  This essentially restricts more than one thread to access the same piece of 
  code in parallel.

You may ask, but how in the above example Thread based execution is faster
than Process based?
- That is because we have introduced a replication of IO bound operation in the 
  form of time.sleep(), whenever a thread encounters such operation it releases 
  its control over the execution until a response comes back. This allows other
  threads to complete their tasks, hence we get the the feeling of parallelism.
  But if we were to do some CPU bound operations like number crunching this will
  essentially perform on par with single threaded execution. This is where 
  ProcessPoolExecutor() comes into picture, as it is actually doing parallelism
  behind the scenes.
"""
