"""
Concurrency:
- doing multiple computations at the same time, or at least creating an illusion
  of doing so.
- before multicore processors came into existence all the computation tasks were
  run by a single core system(obviously), that doesn't mean the tasks couldn't
  be accomplished concurrently.
- most of the tasks were IO bound which means there was a lot of waiting going
  around for tasks like disk writes, network calls and all. While in the wait
  period, the system could actually allocate its processing power to some other
  task, this way it was able to create an illusion of concurrency.
- but tasks which were CPU bound like number crunching still needed to be 
  processed in a sequential manner, as there was no other way of getting around
  it.
- modern computers now have multiple processors which helps us perform CPU bound
  tasks concurrently.

Python provides 3 different mechanisms in the standard library for concurrency:
- threading
- asyncio
- multiprocessing
Threading and asyncio are 2 different mechanisms for handling IO bound
computing, multiprocessing is actually how to use multiple processors.
NOTE: You must be aware of the Global Interpreter Lock(GIL).

Latency & how it leads to IO bound concurrency:
There are mainly 4 parts associated with running a program:
1. Memory
2. CPU
3. Storage
4. Peripherals
- in order for a program to run, the cpu first fetches the program from storage,
  puts in into memory then executes the instructions, these instructions often 
  impacts peripherals, eg. sending something out to the network, the cpu sends 
  information down to the peripheral card and then the card sends it to the 
  outside world.
- each one of these components runs at a different speed and this is where 
  latency comes into picture.
- consider 1 nanosecond = 1/1,000,000,000 s, a intel i7 can run about 100 
  instructions in 1 ns.
- if we multiply this by 100 i.e. 100 ns, this is how much time it takes to talk
  with main memory, so everytime the cpu needs to talk to memory, you need to
  delay by 100 ns. Modern computers have ways to speed this up like L2 caches.
- 1 microsecond = 1000 ns, time to read 500kB from memory
- 1 milisecond = 1000 microseconds, about 2 ms to perform a disk seek operation,
  which is when we ask hard drive to look for something and the read head is not
  on that position right now, takes about 2 ms for the read head to reposition
- 150 ms is the Ping time USA to Europe, packet going out across the Atlantic 
  from the east coast of USA to Europe and coming back.
- the difference between a single instruction and a simple network call is an
  astronomical amount. To put this in perspective: let us consider a scenario
  1 second to perform 1 instruction.
. Referencing memory - 2hrs 47mins - 10k instructions
. Disk seek - 6 years, 4 months - 200M instructions
. Seek + Read 1MB - 8 years, 11 months - 285M instructions
. Ping Europe - 475 years, 8 months - 15B instructions

Timeslicing:
- the idea of operating system mixing other programs into these wait states, 
  while your program is waiting for the network call to finish the computer can
  insert multiple other programs to take advantage of that time. This is how a
  single processor can make it look like it is doing a lot of things at the same
  time.
- there are 3 levels to timeslicing:
1. No multitasking: DOS operating system
2. Cooperative multitasking: Program willing to give up CPU
   Windows 3.1
3. Pre-emptive multitasking: Program can be interrupted by the OS
   Mainframes, Unix based, Windows NT/95 and onwards
- the modern computers have different multiple cpus performing timeslicing and
  the programs may or may not be shared across cpus, all of this is the 
  responsibilty of OS to handle.

Types of Concurrency:
1. Trivial Concurrency: When different parts of the program can be split apart
   without concerns for each other. This is achieved when activities within the
   program are completely independent of one another. There is no shared data.
2. Shared Data Concurrency: Software typically has three steps - input, compute
   & output. Splitting up the compute portion means coordination is required at
   the input & output stages. May also require coordination amongst compute 
   nodes.

Concurrency Patterns:
. Pipeline ~ Producer(Input) - Worker(Compute) - Consumer(Output)
. N - Workers ~ P - N Ws - C
. Broadcast ~ P = N Ws - C
  a variation to above pattern where each worker sees all of the 
  data, it may not operate on all of the data
. MIX-AND-MATCH ~ P = N Ws - N Ws - C

Concurrency Challenges:
. Execution Co-ordination - how to sync up different processes
. Memory allocation - which processes get what memory
. Scheduling - when are which processes active, for the most part you just let 
  the OS handle this for you
. Throughput - getting more work done per unit time by applying above concepts
. Distribution - threads, processes & machines.
. Deadlocks - when 2 or more components are waiting on each other
. Resource starvation - running out of memory, disk space, processes
"""
