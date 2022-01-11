import datetime
import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format=' %(message)s', )

BUF_SIZE = 50
dirty_basket = queue.Queue(BUF_SIZE)
clean_basket = queue.Queue(BUF_SIZE)
queue_log = queue.Queue(BUF_SIZE + BUF_SIZE)
tot_fruit = 50


def producer(id):
    global tot_fruit

    while tot_fruit > 0:

        if not dirty_basket.full():
            threadLock.acquire()
            tot_fruit -= 1
            item = tot_fruit
            dirty_basket.put(item)
            queue_log.put(f'Farmer-{id} ({item})')
            threadLock.release()
            dalay_wait = random.randint(3, 6)
            time.sleep(dalay_wait)
    return


def consumer(id):
    global tot_fruit
    while tot_fruit > 0:
        if not dirty_basket.empty():
            item = dirty_basket.get()
            clean_basket.put(item)
            queue_log.put(f'Cleaner-{id} ({item})')
            dalay_wait = random.randint(2, 4)
            time.sleep(dalay_wait)
    return


def logging_app():
    """
    function to monitor logs displayed by producer and consumer
    :return:
    """
    while tot_fruit > 0:
        time.sleep(1)
        # if str(queue_log.get).startswith("Farmer"):
        # print(queue_log.get())
        logging.debug(
            f' {datetime.datetime.now().replace(microsecond=0)} Tree ({tot_fruit} fruits) - dirty basket ({dirty_basket.qsize()}) '
            f'- Clean Basket ( {clean_basket.qsize()} ) -  '
            f'{queue_log.get()} - '
            f'{queue_log.get()}'

            )
    return


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []

    for i in range(3):
        p = threading.Thread(target=producer, args=(i,), name=f'Farmer-{i}')
        p.start()

        # time.sleep(2)
        c = threading.Thread(target=consumer, args=(i,), name=f'Cleaner-{i}')
        c.start()

        threads.append(p)
        threads.append(c)

    log = threading.Thread(target=logging_app, name=f'Logging')
    log.start()

    threads.append(log)
    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")
