import time
import asyncio


async def calculate(limit):
    await sum(i * i for i in range(limit))


async def find_sums(numbers):
    tasks = []
    for num in numbers:
        task = asyncio.ensure_future(calculate(num))
        tasks.append(task)

    asyncio.gather(*tasks)

if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    print('Starting calculation')
    start = time.monotonic()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(find_sums(numbers))
    duration = time.monotonic() - start
    print(f'Finished computations in {duration:.2f} seconds')
