import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

BUF_SIZE = 50
dirty_basket = queue.Queue(BUF_SIZE)
clean_basket = queue.Queue(BUF_SIZE)
tot_fruit = 3


class TestClass(object):

    def test_find_rigth_path(self):
        retorno = producer(1)
        assert retorno is not None

    def test_find_rigth_path(self):
        retorno = consumer(1)
        assert retorno is not None


def producer(id):
    global tot_fruit
    while tot_fruit > 0:

        if not dirty_basket.full():
            threadLock.acquire()
            tot_fruit -= 1
            item = tot_fruit
            dirty_basket.put(item)
            threadLock.release()
            logging.debug(f'Farmer-{id} ' + f'({item})'
                          + ' : ' + str(dirty_basket.qsize()) + ' Fruit in the dirty basket')
            dalay_wait = random.randint(3, 6)
            time.sleep(dalay_wait)
            return

    return None


def consumer(id):
    global tot_fruit
    while tot_fruit > 0:
        if not dirty_basket.empty():
            item = dirty_basket.get()
            clean_basket.put(item)
            logging.debug(f'Cleaner-{id} ' + f'({item})'
                          + ' : ' + str(clean_basket.qsize()) + ' Fruit in the clean basket')
            # logging.debug('Clean basket ' + str(item)
            #               + ' : ' + str(clean_basket.qsize()) + ' items in queue')
            dalay_wait = random.randint(2, 4)
            time.sleep(dalay_wait)
            return
    return None


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []

    p = threading.Thread(target=producer, args=(1,))
    p.start()

    # time.sleep(2)
    c = threading.Thread(target=consumer, args=(1,))
    c.start()

    threads.append(p)
    threads.append(c)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")
