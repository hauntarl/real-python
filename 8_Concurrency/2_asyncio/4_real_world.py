"""
format - http://qrng.anu.edu.au/API/jsonI.php?length={nums}&type={data_type}
sample - http://qrng.anu.edu.au/API/jsonI.php?length=5&type=uint16

Responses:
- success: {
  "type": "uint16",
  "length": 5,
  "data": [38041, 57363, 29436, 49566, 33087],
  "success": true
}
- failure: {
  "success": false
}

Inorder to make http requests, their are numerous 3rd party packages available.
We will be using aiohttp package for this demonstration. To get the package run
'pip install aiohttp' in your terminal and import it. Speciality of this package
is that, it allows us to make asynchronous calls to outside world.
"""
import asyncio
import time
import json
import aiohttp  # 3rd party library, requires: pip install aiohttp
from random import randint

base_url = 'http://qrng.anu.edu.au/API/jsonI.php'


async def worker(
    name: '<any>',
    length: int,
    data_type: str,
    session: aiohttp.ClientSession
) -> dict:
    """Returns the response generated from GET request made to the API."""
    print(f'worker-{name}')
    # 1. generate request url with query parameters.
    url = f'{base_url}?length={length}&type={data_type}'
    # 2. make the network call and waiting for the response
    response = await session.request(method='GET', url=url)
    # 3. fetching the json string from the response
    value = await response.text()
    # 4. convert the json response to python understandable object and return.
    return json.loads(value)


async def one():
    """Creates a ClientSession and makes a single request to the api."""
    # similar to async for loop, we also have async with, which handles the
    # Client session opening and closing for us, in Python we need to create a
    # Client session in order to make an http request.
    async with aiohttp.ClientSession() as session:
        # 1. call a single worker and wait for the response.
        response = await worker('bob', 4, 'uint8', session)
        # 2. print the response.
        print(f'response: {response}', type(response), sep='\n')


async def work_generator(session: aiohttp.ClientSession) -> dict:
    """Creates a worker, awaits its response, yields the value."""
    for i in range(3):
        r = randint(1, 5)
        response = await worker(i+1, r, 'uint8', session)
        yield response


async def many_for():
    async with aiohttp.ClientSession() as session:
        async for response in work_generator(session):
            print(f'response: {response}')
        # following loop is same as the above one
        # for i in range(3):
        #     r = randint(1, 5)
        #     response = await worker(i+1, r, 'uint8', session)
        #     print(f'response: {response}')


async def many_gather():
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            *(worker(i + 1, randint(1, 5), 'uint8', session)
              for i in range(3))
        )
        for res in responses:
            print(f'response: {res}')


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(one())
    elapsed = time.perf_counter() - start
    print(f'Finished in {elapsed:.4f} secs')

    print()
    start = time.perf_counter()
    asyncio.run(many_for())
    elapsed = time.perf_counter() - start
    print(f'Finished in {elapsed:.4f} secs')

    print()
    start = time.perf_counter()
    asyncio.run(many_gather())
    elapsed = time.perf_counter() - start
    print(f'Finished in {elapsed:.4f} secs')

"""
OUTPUT:
worker-bob
response: {'type': 'uint8', 'length': 4, 'data': [121, 94, 117, 160], 'success': True}
<class 'dict'>
Finished in 0.7662 secs

worker-1
response: {'type': 'uint8', 'length': 4, 'data': [251, 169, 43, 181], 'success': True}
worker-2
response: {'type': 'uint8', 'length': 3, 'data': [120, 135, 34], 'success': True}
worker-3
response: {'type': 'uint8', 'length': 3, 'data': [219, 58, 120], 'success': True}
Finished in 2.6520 secs

worker-1
worker-2
worker-3
response: {'type': 'uint8', 'length': 1, 'data': [49], 'success': True}
response: {'type': 'uint8', 'length': 1, 'data': [52], 'success': True}
response: {'type': 'uint8', 'length': 1, 'data': [114], 'success': True}
Finished in 0.7996 secs

Design Patterns: https://realpython.com/async-io-python/#async-io-design-patterns
I don't understand Python's Asyncio: https://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/
"""
