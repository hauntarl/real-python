"""
Multiprocessing
. Both the threading and asyncio library operate inside of a single Python
  interpreter and therefore are encumbered by the GIL
. If you’re doing I/O-bound concurrency, this typically isn’t a problem. You 
  can still get speed-up because of the long latency waiting for network or 
  disk access. Python has a library called multiprocessing that allows you to 
  spin up an interpreter per CPU.
. This allows you to do CPU-bound concurrency. As each CPU gets its own 
  instance of the interpreter, the GIL isn’t a problem, you get one GIL per CPU.
"""

import multiprocessing
import requests
import time

session = None


def get_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        indicator = multiprocessing.current_process().name[-1]
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=get_session) as pool:
        pool.map(download_site, sites)
    print()


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print('Starting downloads...')
    start = time.monotonic()
    download_all_sites(sites)
    duration = time.monotonic() - start
    print(f'Downloaded {len(sites)} sites in {duration:.2f} seconds.')

"""
. The key lines of code to using the multiprocessing library are the creation 
  of the Pool and the mapping of the data. By default, the Pool creates one 
  process per CPU in your computer.
. Each process has its own memory space and the initializer parameter is called 
  once per process within the local memory of that space. In the case of this 
  example, there are still 160 things to download, so as a single 
  download_site() function finishes, the Pool assigns the next one to whatever 
  CPU is currently idle.
. This could account for some of the numbers repeating themselves. If CPU 4 
  happens to be freed up while 3, 2, and 1 are still waiting on the I/O, 4 
  would get the next download_site(), and if for whatever reason it happened to 
  be able to download quickly, it might print out a result before one of the 
  other three processes finished downloading their site. And once again, 
  because each CPU gets its own instance of the interpreter, you no longer have 
  the problem of the GIL.

Issues
. So if multiprocessing partially solves the GIL problem, why wouldn’t you just 
  do this all the time? Well, first off, it requires a lot of overhead to 
  create a process.
. The implementation of a process happens at the operating system level, so you 
  will also see behavior and scheduling differences between operating systems 
  in your code. Because each process gets its own copy of the interpreter, it 
  tends to require more memory than threading does as well.
. And not only does it require more memory, but you have to spin up the 
  interpreter, so the initialization time of each process tends to be longer 
  than threads.
. In fact, threads were introduced into operating systems as a lightweight way 
  of getting around the overhead involved in processes. Because each process 
  has its own interpreter and does not share memory footprints, communicating 
  between the processes must be done with explicit constructs.

Communication
. The multiprocessing library comes with a few that can help you do that. Queue 
  and Pipe are ways of sending data from one process to another, and the Value 
  and Array constructs allow you to share memory between processes.
. The multiprocessing library includes locking mechanisms to make sure that you 
  don’t end up with race conditions or deadlocks when two or more processes are 
  trying to access the same chunk of shared memory.
. The number of threads that you instantiate generally can be as many as you 
  want. More is not always better, but it’s under your control. multiprocessing 
  typically is only used to map processes to CPUs.
. You can instantiate more interpreters than CPUs, but it doesn’t really make 
  sense because then all you’re doing is swapping out those and the overhead of 
  the swap tends to be more expensive and you don’t actually gain any speed-up.

NOTE: threading and asyncio tend to be beneficial in I/O-bound situations. 
  They’re not beneficial in CPU-bound situations. That’s where multiprocessing 
  reigns.
"""
