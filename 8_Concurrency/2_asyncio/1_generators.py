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
