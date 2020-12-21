import collections
import time
import multiprocessing
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


# this function tries to replicate some action which takes a lot of time to
# finish so that we can see why and how multiprocessing helps us reduce the
# time for execution and improve the performance of our program
def transform(x):
    print(f'Process {os.getpid()} is working on {x.name}...')
    time.sleep(1)
    result = {'name': x.name, 'age': 2020 - int(x.born)}
    print(f'Process {os.getpid()} finished processing {x.name}.')
    return result


# Sequential - comment Parallel and run this block
# start = time.time()
# result = tuple(map(
#     transform,
#     scientists
# ))
# end = time.time()
# print(f'\nSequential finished in {end - start:.2f}s.')
# pprint(result)

# Parallel - comment Sequential and run this block
if __name__ == '__main__':
    """
    NOTE: this type of code structuring is required in Python 3.8, create a
    if __name__ == '__main__' block and create a pool object using the context
    manager syntax for the code to work properly. You can remove this block to
    see the exception which Python throws if you using 3.8.

    - processes: argument determines how many processes should be created for
      the execution of following code, processes=1 behaves like sequential
    - maxtasksperchild: argument determines how many tasks should be assigned to
      one process before it restarts.

    If we leave out all the arguments, the pool will by default spawn as many
    processes as you have cpu cores.
    """
    with multiprocessing.Pool(processes=len(scientists), maxtasksperchild=1) as pool:
        start = time.monotonic()
        result = pool.map(transform, scientists)
        end = time.monotonic()
        print(f'\nParallel finished in {end - start:.2f}s.')
        pprint(result)
