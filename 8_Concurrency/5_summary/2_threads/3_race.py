from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import threading
from functools import reduce

counter = 0
thread_iter = dict()


def change_counter(amount):
    global counter
    """
    In Synchronous mode:
    - the race condition doesn’t happen yet. A -1 is added to the counter 
      10,000 times, then 1 is added to the counter 10,000 times, and it does 
      that for 998 more times, the end result being 0.
    
    In Asynchronous mode:
    - That’s not 0. And this is the problem. From a mathematics standpoint, the 
      reason this is failing is line 7. You can think of that for loop like a 
      multiplier. In the synchronous case, -1 is multiplied by 10,000 and added,
      and then 1 is multiplied by 10,000 and added, and you result in 0. 
    - In the threaded case, you get partway through that multiplication. So 
      instead of it being 10,000 times -1, it might be 500 times -1, and then 
      the other case comes in. That might be 600 times 1, giving you a delta.
    - The sum total of the multiplication factors is not the same as the 
      synchronous addition, so you get a race condition. You get the wrong 
      number. Not only is it the wrong number, it’s not even consistently the 
      wrong number.
    - If I run this again, I get a different result. And this is because the 
      scheduling changes how things are happening. The effect of the multiplier 
      is different this time through because the amount of time each thread is 
      run is different, and you get a different number.
    - This is an exaggerated example. Race conditions generally are far more 
      subtle than this, and it would be far harder to find the problem if one 
      in a hundred executions actually caused the bug to happen, and that’s a 
      common result in race conditions. It makes them nasty to find.
    """
    # to keep track of all the threads and total iterations each one is doing
    # along with the amount value that thread has been assigned
    if (threading.get_ident(), amount) not in thread_iter:
        thread_iter[(threading.get_ident(), amount)] = 0

    for _ in range(10000):
        thread_iter[(threading.get_ident(), amount)] += 1
        counter += amount


def race(num_threads):
    global counter
    counter = 0
    data = [-1 if x % 2 else 1 for x in range(1000)]

    # when the num_threads value is 1, the program is synchronous
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(change_counter, data)

    pprint(thread_iter)
    print(f'\ncounter value(ideally should be 0): {counter}')
    print(f'total iterations (1,000 x 10,000): {sum(thread_iter.values())}')

    delta = sum([v if k[1] > 0 else - v for k, v in thread_iter.items()])
    print(f'delta (positive iterations - negative iterations): {delta}')


if __name__ == '__main__':
    # race(1)
    race(5)  # increase num_threads to consistently achieve race condition

"""
OUTPUT: 
{(1272, -1): 960000,
 (1272, 1): 1020000,
 (5704, -1): 940000,
 (5704, 1): 930000,
 (7960, -1): 1000000,
 (7960, 1): 1050000,
 (12428, -1): 1000000,
 (12428, 1): 900000,
 (12800, -1): 1100000,
 (12800, 1): 1100000}

counter value(ideally should be 0): 111490
total iterations (1,000 x 10,000): 10000000
delta (positive iterations - negative iterations): 0
"""
