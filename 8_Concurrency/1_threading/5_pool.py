"""
In this program, we will try to reduce the amount of code that we needed to
write and use something called as thread pool executor to manage the starting
and the joining of the threads.
"""

import concurrent.futures
import time


def func(name):
    print(f'func started with arg {name}')
    time.sleep(2)
    print(f'func ended with {name}')


if __name__ == '__main__':
    print('main started')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(func, ['foo', 'bar', 'baz'])
    print('main ended')
"""
NOTE: there is no guranteed order in which the func gets executed, even if we
are sequentially creating the threads and running them, the scheduling depends
on the how the operating system is able to allocate cpu to them. This is called
a race condition where every thread tries to get access to the cpu without 
knowing the existence of others, hence not communicating with each other.

This is not an issue in our existing example as they are all performing tasks
which are independent of one another. But if they were to operate on a shared 
variable then that might cause some serious issues. eg. for a given bank balance
of $100 if a person were to deposit $50 and immediately tried to see their 
available balance, because of the race condition where both threads are trying 
to gain access to the shared variable, one wants to write and one to read, their
is no gurantee that the write operation will occur before the read and person
may see their balance as $100 even after depositing more money. This in real 
world could cause some serious issues and any banking system would want to avoid
that.

Race Condition: more than one threads are trying to access the shared piece of
data at the same time.
"""
print()


class Account:
    def __init__(self):
        self.balance = 100  # shared data

    def update(self, transaction, amount):
        print(f'{transaction} thread updating...')
        local_copy = self.balance
        local_copy += amount
        time.sleep(1)
        self.balance = local_copy
        print(f'{transaction} thread finishing...')


if __name__ == '__main__':
    account = Account()
    print(f'Starting with balance of {account.balance}')
    # NOTE: if you change the max_workers variable to 1, it will behave like a
    # single threaded application and we won't be able to examine the race
    # condition because there is only 1 thread alive at any given point of time.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [('deposit', 50), ('withdrawal', -150)]:
            ex.submit(account.update, transaction, amount)

    print(f'the ending balance of {account.balance}')
"""
Initially the deposit thread starts the execution, it creates a local copy and
adds the given amount to it, then it goes to sleep, at this point the value of
local copy is 150 but self.balance is still 100. As deposit thread is sleeping
withdrawal thread can start its execution, it reads the balance and creates a 
local copy which will have the balance as 100, local copy gets updated with the
withdrawal amount and becomes -50, the withdrawal thread now goes to sleep for
1 second. Meanwhile deposit thread wakes up and updates the balance from local
copy to 150. Later withdrawal thread updates the balance from its local copy to
-50. We can cleary see the conflict here.
"""
