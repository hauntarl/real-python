"""
This version of the program uses the N-Workers Pattern
- download_all_sites() acts as a producer
- download_site() acts as the worker, here concurrent.futures dictates the 
  number of workers
- executor acts as a collection point, it waits until all of threads are 
  finished and once they are, the program continues as before once the pool 
  passes execution on
NOTE: This program technically doesn't have a consumer, download_site() is 
throwing out the data and not doing any computations on it.
"""

import concurrent.futures
import threading
import requests
import time

"""
Thread Safety:
- Memory is shared across all the threads
- Consider two threads using a single requests.Session() object
- thread 1 starts downloading from Jython, gets interrupted
- thread 2 starts downloading from RealPython, but the session object wasn't
  done (deadlock)

Solution:
- Low-level primitives fix this using a mechanism called locking, Python already
  has GIL which is at the Global level, our program has the same problem
- Fortunately, Python comes with a library method which makes this easier,
  threading.local()
- this is actually creating a locked space for your objects which are created
  once per thread
- get_session() creates a new request.Session() object per thread, which 
  guarantees that each thread gets its own requests.Session object, also means
  that you won't create 60 requests.Session objects for your 60 urls
"""
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    """
    More threads for the win?
    - Thread Pool size is set to 5, even though we are downloading 60 urls
    - There is overhead for creating threads
    - There is overhead for switching between threads
    - Too many threads also means code spends all its time managing them
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)
    print()


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 30

    print('Starting downloads...')
    start = time.monotonic()
    download_all_sites(sites)
    duration = time.monotonic() - start
    print(f'Downloaded {len(sites)} sites in {duration:.2f} seconds.')

"""
Thread primitives:
- Thread.start() - responsible for creating the threads and calling the 
  appropriate functions
- Thread.join() - point in the program that waits for all the threads to finish
- Queue - a thread-safe mechanism for communicating between the threads

The concurrent.futures library and Executors abstracts these away
"""
