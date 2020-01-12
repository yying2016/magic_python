from threading import Thread
import random
import time
from queue import Queue


class Producer(Thread):
    def __init__(self, queue, to_process):
        Thread.__init__(self)
        self.queue = queue
        self.to_process = to_process

    def run(self):
        for item in self.to_process:
            #item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify: item N0 {} appended to queue by {}'.format(item, self.name))
            time.sleep(1)


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            try:
                print('Consumer notify: {} poped from queue by {}'.format(item, self.name))
            finally:
                self.queue.task_done()


def main():
    to_process = [1, 2, 3, 4, 5]
    queue = Queue()
    for item in to_process:
        queue.put(item)

    # t1 = Producer(queue, to_process)
    # t1.start()

    for i in range(4):
        t = Consumer(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        t.daemon = True
        t.start()

    queue.join()
    print("End!")


if __name__ == "__main__":
    # queue = Queue()
    # t1 = Producer(queue)
    # t2 = Consumer(queue)
    # t3 = Consumer(queue)
    # t4 = Consumer(queue)
    #
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    main()









