"""
The producer is going to produce some piece of data and is going to put it on 
the conveyor belt. When the consumer receives this data, it will do something 
with it.

Mechanism like this is used in all kinds of software, you might see this in a
message queing system, data pipelines doing ETL work.

We will create a producer consumer pipeline in a multithreaded context in a 
thread safe mannner(hopefully).
"""
import random
import time
import threading
import concurrent.futures

FINISH = 'THE END'
producer_pipeline = []
consumer_pipeline = []


class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # locking the consumer thread at initialization restricts the consumer
        # from consuming a message before the producer has produced any.
        self.consumer_lock.acquire()

    def set_message(self, message):
        # acquiring the producer lock to write message, this lock restricts
        # the producer from writing new message before consumer has consumed the
        # previous one.
        self.producer_lock.acquire()
        print(f'Producing message of {message}')
        producer_pipeline.append(message)
        self.message = message
        # releasing the consumer lock, now that message queue has atleast one
        # message written by producer, consumer is free to read from it
        self.consumer_lock.release()

    def get_message(self):
        # acquiring the lock to read from the message queue, this lock restricts
        # the consumer from reading the message before producer has produced a
        # new one.
        self.consumer_lock.acquire()
        print(f'Consuming message of {self.message}')
        message = self.message
        consumer_pipeline.append(message)
        # releasing the producer lock, allowing it to write new data to the
        # message queue.
        self.producer_lock.release()
        return message


def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)

    pipeline.set_message(FINISH)


def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())


if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exe:
        exe.submit(producer, pipeline)
        exe.submit(consumer, pipeline)
    print(f'producer: {producer_pipeline}')
    print(f'consumer: {consumer_pipeline}')
"""
Creating a pipeline is this way can be really cumbersome and unsafe, as the 
developer has to keep track of acquiring and releasing of the locks, the 
program can go really wrong with one tiny mistake.

The current example also has one more limitations in terms of how many producers
and consumers can be used. Its 1 for each, also as noticed the rate of producer
producing a new message is faster than consumer consuming it. We block the 
producer from generating a new message until consumer has finished consuming it,
which is not ideal. We also need some sort of buffer or queue which will be 
capable of handling the variation in speeds between producer and consumer.

queue module does all that.
"""
