"""
Asynchronous Generators are an amalgamation of python generators and coroutines.
Its a generator that produces values, but at the same time, it does it 
asynchronously. 1st value may come out 1 second later, 2nd may come out 10 
seconds later and so on...
"""
import asyncio
from random import randint


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


async def square_odds(start, stop):
    for odd in odds(start, stop):
        r = randint(1, 3)
        await asyncio.sleep(r)
        yield odd, odd ** 2, r


async def main():
    """
    normally when you have a generator you use a for-in loop, but this is an 
    async-generator so we will have to use async for-in loop
    """
    async for odd, sqo, took in square_odds(11, 17):
        print(f'square of odd: {odd} is {sqo}, took: {took} seconds.')


if __name__ == '__main__':
    asyncio.run(main())
