"""
Asyncio
. the threading library is dependent on threads supported by the OS
. aysncio is Python specific and is independent of the OS, this gives you finer
  grain control over your concurrency
. this model uses event loop and coroutines
. event loop: a main loop that happens inside of Python which controls the
  order of things that are happening
. coroutine: the code that is being run, inside of the code, you signal you no
  longer need control and you give up execution. The event loop then schedules
  the next coroutine
. this is called co-operative concurrency, if one of the tasks doesn't give up
  control the other tasks starve, since all of this is happening inside of your
  Python code, you aren't fighting with some other program having to be
  co-operative. Its your own code and you're in control, as long as you write
  good coroutines, you won't have a problem
. keywords:
    - async - indicates that the code needs to be run asynchronously
    - await - co-operative signal that your coroutine is willing to give up
              their execution control

Challenges
. asyncio is fairly new
. to take advantage of it, the libraries you're using have to support it
. requests library doesn't currently support asyncio(Jan 2021), need to use
  aiohttp, similar to requests but it is asyncio aware
. aiohttp is not part of the Python standard library, to install do
  'python -m pip install aiohttp'

Asyncio version of webpage downloader
"""
import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)
        """
        error handling
        . return_exceptions dictates what to do if something goes wrong
        . cases:
            - False - causes a normal exception and stops the program (default)
            - True  - registers the exception in the task object 
        . tasks can be introspected if value is set to True

        Task.result() will return result of the coroutine or raise:
        . exception caused by task
        . CancelledError - when we request the event loop to cancel running task
        . InvalidStateError - when we call the result method too early and
          the task hasn't finished operating or hasn't been cancelled
        """

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print('Starting downloads...')
    start = time.monotonic()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_sites(sites))
    duration = time.monotonic() - start
    print(f'\nDownloaded {len(sites)} sites in {duration:.2f} seconds.')

"""
Threads vs asyncio
. asyncio concurrency requires less overhead as it is managed in Python itself,
  it tends to out-perform threads
. coding with asyncio is a little more complicated
. asyncio is still new
. threading is pre-emptive multitasking, asyncio is co-operative multitasking
"""
