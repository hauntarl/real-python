"""
At the heart of async IO are coroutines. A coroutine is a specialized version 
of a Python generator function. Let’s start with a baseline definition and then 
build off of it as you progress here: a coroutine is a function that can 
suspend its execution before reaching return, and it can indirectly pass 
control to another coroutine for some time.

Similar to generators, they can be stopped and paused and restarted,
but they are different in the sense that, generators generate values and
coroutines consume them. You can think of generators as Producers and coroutines
as Consumers of data.

def randn():
    time.sleep(3)
    return randint(1, 10)

>>> randn()  # this will take 3 seconds to execute and return the value
8
>>> [randn() for _ in range(3)]  # this will take around 9 seconds
[2, 5, 9]

- now will we convert the same function into a coroutine.

def randn():
    asyncio.sleep(3)
    return randint(1, 10)

>>> randn()  # this will instantaneously return a random value with a warning
RuntimeWarning: coroutine 'sleep' was never awaited
7

So, now our function is registered as coroutine in python. In order to achieve
the desired result we need to use the await keyword on the sleep() method.
"""
import asyncio
import time
from random import randint


async def randn():
    """
    You might get confused that, does this thing waits for 3 seconds similar to
    time.sleep() and then return the value. Well actually is does and does not.

    It means that any code that happens after the await call, will not happen
    until await is finished. But it doesn't stop the execution at the caller's
    end, they will keep on executing in a normal way. You can imagine this as a
    task running in background, it will notify you when the task is done, then
    you can continue with the execution for the rest of the fucntion.

    NOTE: you can only use the await keyword inside an async function, if not
    then python will throw an error saying: await was called outside async func.
    You make a function async by using the async keyword before def keyword.
    """
    await asyncio.sleep(3)
    return randint(1, 10)


"""
>>> randn()  # gives you a coroutine object, with the same warning as before.
<coroutine object randn at 0x000001C8E86053C0>
RuntimeWarning: coroutine 'randn' was never awaited
  randn()  # gives you a coroutine object, with the same warning as before.
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

- to fetch the value from a coroutine, you can't just simply call the function
and expect it to return a value. You also have to await on the coroutine
because randn() is also asynchronous now.

def async_main():
    r = await randn()
>>> async_main()  # throws an error: await was called outside async func.


# making async_main() async as well
async def async_main():
    r = await randn()
>>> async_main()
RuntimeWarning: coroutine 'async_main' was never awaited

- what is going on?
We need to create an event loop, event loop is actually going to run all these
async functions. What the heck is an event loop?
https://www.youtube.com/watch?v=8aGhZQkoFbQ&list=LLGW1hymhJhF0qhSMYOuvmIg&index=9&t=0s
"""


async def main(async_func, *coroutines):
    start = time.perf_counter()
    res = await async_func(*[f() for f in coroutines])
    elapsed = time.perf_counter() - start
    print(f'{res} took: {elapsed:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main(randn))
    # this will create the event loop we so desperately need. It will handle
    # all the asynchronous tasks for us.
    # if you notice the output, you might ask, why do we even need this? It
    # still takes 3 seconds to run my code.

    # let's do numerous randn() calls at the same time
    asyncio.run(main(asyncio.gather, randn, randn, randn))
    # NOTE: this only took 3 seconds
    # asyncio.gather() will collectively wait for all functions calls to be
    # executed and then return their result as a collection.

    # lets create 10 coroutines and run them to see the result
    asyncio.run(main(asyncio.gather, *(randn for _ in range(10))))
    # you might be actually thinking that this would create a tuple
    # comprehension, but instead it creates a generator and the * causes the
    # generator to run and then also takes care of unpacking of those results.
    gen = (x for x in range(10))
    print(*gen, sep='->')

"""
You can think of this as running in parallel, but they are not. What's actually
happening is, its actually running only on one thread, its telling the system to
sleep, the os is handling the sleeping. Once it is done sleeping, the os comes
back and says, hey python I am done with all these 10 tasks at basically the
same amount of time, then python processes those.

Sleeping doesn't really happen in python, it happens outside python basically
in the operating system.


- Another example:

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

- output:
One
One
One
Two
Two
Two
countasync.py executed in 1.01 seconds.

The order of this output is the heart of async IO. Talking to each of the calls 
to count() is a single event loop, or coordinator. When each task reaches await 
asyncio.sleep(1), the function yells up to the event loop and gives control 
back to it, saying, “I’m going to be sleeping for 1 second. Go ahead and let 
something else meaningful be done in the meantime.”

While using time.sleep() and asyncio.sleep() may seem banal, they are used as 
stand-ins for any time-intensive processes that involve wait time. (The most 
mundane thing you can wait on is a sleep() call that does basically nothing.) 
That is, time.sleep() can represent any time-consuming blocking function call, 
while asyncio.sleep() is used to stand in for a non-blocking call (but one that 
also takes some time to complete).


The Rules of Async IO:
- The syntax async def introduces either a native coroutine or an asynchronous 
  generator. The expressions async with and async for are also valid, and 
  you’ll see them later on.
- The keyword await passes function control back to the event loop. (It 
  suspends the execution of the surrounding coroutine.) If Python encounters an 
  await f() expression in the scope of g(), this is how await tells the event 
  loop, “Suspend execution of g() until whatever I’m waiting on—the result of 
  f()—is returned. In the meantime, go let something else run.”

async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r

There’s also a strict set of rules around when and how you can and cannot use 
async/await.
- A function that you introduce with async def is a coroutine. It may use 
  await, return, or yield, but all of these are optional. Declaring 
  'async def noop(): pass' is valid:
- Using await and/or return creates a coroutine function. To call a coroutine 
  function, you must await it to get its results.
- It is less common (and only recently legal in Python) to use yield in an 
  async def block. This creates an asynchronous generator, which you iterate 
  over with async for. Forget about async generators for the time being and 
  focus on getting down the syntax for coroutine functions, which use await 
  and/or return.
- Anything defined with async def may not use 'yield from', which will raise a 
  SyntaxError.
- Just like it’s a SyntaxError to use yield outside of a def function, it is a 
  SyntaxError to use await outside of an async def coroutine. You can only use 
  await in the body of coroutines.

async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y

- Finally, when you use await f(), it’s required that f() be an object that is 
  awaitable. Well, that’s not very helpful, is it? For now, just know that an 
  awaitable object is either (1) another coroutine or (2) an object defining an 
  .__await__() dunder method that returns an iterator. If you’re writing a 
  program, for the large majority of purposes, you should only need to worry 
  about case #1.


That brings us to one more technical distinction that you may see pop up: an 
older way of marking a function as a coroutine is to decorate a normal def 
function with @asyncio.coroutine. The result is a generator-based coroutine. 
This construction has been outdated since the async/await syntax was put in 
place in Python 3.5.

These two coroutines are essentially equivalent (both are awaitable), but the 
first is generator-based, while the second is a native coroutine:

@asyncio.coroutine
def py34_coro():
    '''Generator-based coroutine, older syntax'''
    yield from stuff()

async def py35_coro():
    '''Native coroutine, modern syntax'''
    await stuff()

If you’re writing any code yourself, prefer native coroutines for the sake of 
being explicit rather than implicit. Generator-based coroutines will be removed 
in Python 3.10.
"""
