"""
asyncio is a library built into python to write concurrent code using the
async/await syntax.
- concurrency is not parallelism: things that are concurrent are tasks or items
that could potentially run in parallel but may not necessarily run in parallel.

It is often a perfect fit for IO-bound and high-level structured network code.
- IO-bound: if your application's performance mainly depends IO and the reason 
its slow is because of IO then it is called an IO-bound app. eg. reading to a 
file system, reading to a database, talking to a website.

If your code is CPU-bound, consider using the multiprocessing library instead.
Multiprocessing involves creation of new processes to cater to your needs.
If your application is doing a lot of cpu intensive tasks eg. calculating lots
of different prime numbers, then it can leverage multiple processes to perform
the operation.

- asyncio: its only one process and only one thread is doing all the work.
How it works will be explored further in this tutorial.
"""
from random import randint
import time
import asyncio


# Generators:
def odds(start, stop):
    """
    generators: something in python that produces a sequence of values.

    This function generates a sequence of odd values from a given starting point
    to a given endpoint. When this function is called, it actually doesn't run
    this and return values, instead it returns a generator object.

    To fetch values from this generator function, you need to use the built in
    function next() on the generator object.

    This func uses special keyword called yield, what yield does is, it returns
    value to the caller and pauses further execution of the function, when 
    another caller makes a call to this function, yield will resume its 
    execution, generate another value, return it, pause the execution. This can
    keep repeating for infinite times, but here we are restricting it to
    (stop - start) times.

    Once the generator reaches its limit, it returns a StopIteration exception
    which informs the caller that this is the end.
    """
    for odd in range(start, stop + 1, 2):
        yield odd


g1 = odds(3, 15)
print(g1)
print(next(g1))  # one way of fetching the values

g2 = odds(3, 15)
print(list(g2))  # will store all the values in a list
# when you call list() of generator, it internally calls next() until the
# generator exausts. list() internally handles the StopIteration exception.
# NOTE: one risk with using list() on generator objects is that, generators
# can produce infinite values, if you are to store them all in a list, you
# probably will run out of memory and the program will crash.

g3 = odds(3, 15)
odd_nums = []
for o in g3:
    if o == 13:
        break
    odd_nums.append(o)

print(odd_nums)
# another way of iterating over all the values of generator. Here even if the
# generator is infinite, we have the option to introduce our own breakpoint to
# avoid the system from crashing.


def main():
    # using list comprehension
    odds1 = [odd for odd in odds(7, 21)]
    print(odds1)
    # creating a tuple
    odds2 = tuple(odds(21, 29))
    print(odds2)


if __name__ == '__main__':
    print()
    main()


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
What needs to happen is, we need to create an event loop, event loop is actually
what's going to run all these async functions.
What the heck is an event loop? https://www.youtube.com/watch?v=8aGhZQkoFbQ&list=LLGW1hymhJhF0qhSMYOuvmIg&index=9&t=0s
"""


async def async_main(async_func, *coroutines):
    start = time.perf_counter()
    res = await async_func(*[f() for f in coroutines])
    elapsed = time.perf_counter() - start
    print(f'{res} took: {elapsed:.2f} seconds')


if __name__ == '__main__':
    print()
    asyncio.run(async_main(randn))
    # this will create the event loop, we so desperately need. It will handle
    # all the asynchronous tasks for us.
    # if you notice the output, you might ask, why do we even need this? It
    # still takes 3 seconds to run my code.

    # let's do numerous randn() calls at the same time
    asyncio.run(async_main(asyncio.gather, randn, randn, randn))
    # NOTE: this only took 3 seconds
    # asyncio.gather() will collectively wait for all functions calls to be
    # executed and then return their result as a collection.

    # lets create 10 coroutines and run them to see the result
    asyncio.run(async_main(asyncio.gather, *(randn for _ in range(10))))
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
