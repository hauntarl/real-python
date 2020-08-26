"""
- Where Does Async IO Fit In?

Concurrency and parallelism are expansive subjects that are not easy to wade 
into. While this tutorial focuses on async IO and its implementation in Python, 
it’s worth taking a minute to compare async IO to its counterparts in order to 
have context about how async IO fits into the larger, sometimes dizzying puzzle.

Parallelism consists of performing multiple operations at the same time. 
Multiprocessing is a means to effect parallelism, and it entails spreading 
tasks over a computer’s central processing units (CPUs, or cores). 
Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and 
mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. It suggests that 
multiple tasks have the ability to run in an overlapping manner. (There’s a 
saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns 
executing tasks. One process can contain multiple threads. Python has a 
complicated relationship with threading thanks to its GIL, but that’s will be
explored in the coming tutorials.

What’s important to know about threading is that it’s better for IO-bound tasks.
While a CPU-bound task is characterized by the computer’s cores continually 
working hard from start to finish, an IO-bound job is dominated by a lot of 
waiting on input/output to complete.

To recap the above, concurrency encompasses both multiprocessing (ideal for 
CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is 
a form of parallelism, with parallelism being a specific type (subset) of 
concurrency. The Python standard library has offered longstanding support for 
both of these through its multiprocessing, threading, and concurrent.futures 
packages.

Now it’s time to bring a new member to the mix. Over the last few years, a 
separate design has been more comprehensively built into CPython: asynchronous 
IO, enabled through the standard library’s asyncio package and the new async 
and await language keywords. To be clear, async IO is not a newly invented 
concept, and it has existed or is being built into other languages and runtime 
environments, such as Go, C#, or Scala.

In fact, async IO is a single-threaded, single-process design: it uses 
cooperative multitasking, a term that you’ll flesh out by the end of this 
tutorial. It has been said in other words that async IO gives a feeling of 
concurrency despite using a single thread in a single process. Coroutines (a 
central feature of async IO) can be scheduled concurrently, but they are not 
inherently concurrent.

To reiterate, async IO is a style of concurrent programming, but it is not 
parallelism. It’s more closely aligned with threading than with multiprocessing 
but is very much distinct from both of these and is a standalone member in 
concurrency’s bag of tricks.

What does it mean for something to be asynchronous?
- Asynchronous routines are able to “pause” while waiting on their ultimate 
  result and let other routines run in the meantime.
- Asynchronous code, through the mechanism above, facilitates concurrent 
  execution. To put it differently, asynchronous code gives the look and feel 
  of concurrency.

Diagram: https://files.realpython.com/media/Screen_Shot_2018-10-17_at_3.18.44_PM.c02792872031.jpg

Async IO may at first seem counterintuitive and paradoxical. How does something 
that facilitates concurrent code use a single thread and a single CPU core?


- Example:

Chess master Judit Polgár hosts a chess exhibition in which she plays multiple 
amateur players. She has two ways of conducting the exhibition: synchronously 
and asynchronously.

Assumptions:
- 24 opponents
- Judit makes each chess move in 5 seconds
- Opponents each take 55 seconds to make a move
- Games average 30 pair-moves (60 moves total)

Synchronous version: Judit plays one game at a time, never two at the same 
time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 
seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 
12 hours.

Asynchronous version: Judit moves from table to table, making one move at each 
table. She leaves the table and lets the opponent make their next move during 
the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 
minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or 
just 1 hour.

There is only one Judit Polgár, who has only two hands and makes only one move 
at a time by herself. But playing asynchronously cuts the exhibition time down 
from 12 hours to one. So, cooperative multitasking is a fancy way of saying 
that a program’s event loop (more on that later) communicates with multiple 
tasks to let each take turns running at the optimal time.

Async IO takes long waiting periods in which functions would otherwise be 
blocking and allows other functions to run during that downtime. (A function 
that blocks effectively forbids others from running from the time that it 
starts until the time that it returns.)


- Async IO Is Not Easy:

I’ve heard it said, “Use async IO when you can; use threading when you must.” 
The truth is that building durable multithreaded code can be hard and 
error-prone. Async IO avoids some of the potential speedbumps that you might 
otherwise encounter with a threaded design.

But that’s not to say that async IO in Python is easy. Be warned: when you 
venture a bit below the surface level, async programming can be difficult too! 
Python’s async model is built around concepts such as callbacks, events, 
transports, protocols, and futures—just the terminology can be intimidating. 
The fact that its API has been changing continually makes it no easier.

Luckily, asyncio has matured to a point where most of its features are no 
longer provisional, while its documentation has received a huge overhaul and 
some quality resources on the subject are starting to emerge as well.

NOTE: Be careful what you read out there on the Internet. Python’s async IO API 
has evolved rapidly from Python 3.4 to Python 3.7. Some old patterns are no 
longer used, and some things that were at first disallowed are now allowed 
through new introductions. For all I know, this tutorial will join the club of 
the outdated soon too.
"""
