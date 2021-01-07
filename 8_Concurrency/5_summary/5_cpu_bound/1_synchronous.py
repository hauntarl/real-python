"""
. All of the examples up until now have been I/O-bound. In an I/O-bound 
  program, the vast majority of the time the program spends running is in 
  waiting for input and output. Downloading content from the web is a perfect 
  example.
. The amount of latency involved in network transactions far outweighs the 
  computation involved in downloading it. Not all software is I/O-bound. If 
  you’re doing heavy mathematical computations, then most of the time is spent 
  in computation.
. The threading and asyncio libraries only see speed-up in I/O-bound cases, and 
  that’s because they are scheduling computation while the other threads are 
  waiting for the I/O.
. You get speed-up because you’re not waiting for one piece of I/O at a time, 
  you’re waiting for multiple pieces of I/O at a time. 
. If your program instead is doing something that requires a lot of work inside 
  of the CPU rather than waiting on a peripheral, then threading and asyncio is 
  not going to give you that kind of improvement. To get improvement in 
  CPU-bound software, you need multiple CPUs working simultaneously.
"""
import time


def calculate(limit):
    return sum(i * i for i in range(limit))


def find_sums(numbers):
    for num in numbers:
        calculate(num)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    print('Starting calculation')
    start = time.monotonic()
    find_sums(numbers)
    duration = time.monotonic() - start
    print(f'Finished computations in {duration:.2f} seconds')
