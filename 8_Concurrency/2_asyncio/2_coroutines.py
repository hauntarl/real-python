"""
coroutines: similar to generators, they can be stopped and paused and restarted,
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

- so now our function is registered as coroutine in python. In order to achieve
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
    you can continue with the execution of the rest of the fucntion.

    NOTE: you can only use the await keyword inside and async function, if not
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

"""
You can think of this as running in parallel, but they are not. What's actually
happening is, its actually running only on one thread, its telling the system to
sleep, the os is handling the sleeping. Once it is done sleeping, the os comes
back and says, hey python I am done with all these 10 tasks at basically the
same amount of time, then python processes those.

Sleeping doesn't really happen in python, it happens outside python basically
in the operating system.
"""
gen = (x for x in range(10))
print(*gen, sep='->')
