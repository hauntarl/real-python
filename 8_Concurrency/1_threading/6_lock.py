"""
Locks are helpful in preventing the race conditions and undesired outcomes.
"""


import threading
import concurrent.futures
import time


lock = threading.Lock()
print(lock)  # when we create a lock, it is initially in an unlocked state
lock.acquire()  # to set the state to lock, we try to acquire it
print(lock)
# what acquires the lock the is the threading which is executing that piece of
# code, in this case it is the main thread.
# any code below the acquire statement can only be accessed by the current
# thread and no other thread and manipulate it
lock.release()  # to set the state to unlock
print(lock)
"""
We can also use a context manager as an alternative to repeatedly writing lock
and unlock statements.
"""


class Account:
    def __init__(self):
        self.balance = 100  # shared data
        self.lock = threading.Lock()

    def update(self, transaction, amount):
        # restrict simultaneous access to the following block of code
        with self.lock:
            print(f'{transaction} thread updating...')
            local_copy = self.balance
            local_copy += amount
            time.sleep(1)
            self.balance = local_copy
        # -------end of block-------

        print(f'{transaction} thread finishing...')


if __name__ == '__main__':
    print()
    account = Account()
    print(f'Starting with balance of {account.balance}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [('deposit', 50), ('withdrawal', -150)]:
            ex.submit(account.update, transaction, amount)

    print(f'the ending balance of {account.balance}')


"""
Deadlock: Happens when a thread tries to acquire a lock that is already locked

lock = threading.Lock()
lock.acquire()
lock.acquire()
lock.release()  # code never reaches here

this issue may arise due to developer neglegance that may occur when not using
the context manager.

another way to tackle this issue is by using the re-entrant lock, it basically
allows you to make multiple calls to acquire without introducing deadlock.
"""
print()
rlock = threading.RLock()
print(rlock)
rlock.acquire()
print(rlock)
rlock.acquire()
print(rlock)
rlock.release()
print(rlock)
rlock.release()
print(rlock)
"""
there are 2 components to this:
- owner: id for the thread which has acquired the lock
- count: which determines how many locks the current owner has acquired
"""
print(threading.current_thread())  # gives us information about current thread
