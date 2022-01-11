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

import unittest
class TestClass(unittest.TestCase):

    def test_name_producer(self):
        p = threading.Thread(target=producer, name='Cleaner-1')
        p.start()
        self.assertEqual("Cleaner-1", p.getName(), "Nome diferente do esperado")


    def test_name_consumer(self):
        c = threading.Thread(target=consumer, name='Cleaner-1')
        c.start()
        self.assertEqual("Cleaner-1", c.getName(), "Nome diferente do esperado")


    def test_consumer_alive(self):
        c = threading.Thread(target=consumer, name='Cleaner-1')
        c.start()
        self.assertTrue(c.is_alive(), "Consumer alive to read from queue")


    def test_extract_from_tree_failed(self):
        global tot_fruit
        tot_fruit = -1
        p = threading.Thread(target=producer, name='Farmer-1')
        p.start()
        self.assertEqual(p.is_alive(), False, "Não deve ser ativa pelo fato de não ter frutas (tot_fruit = -1) ")

    def test_extract_from_tree(self):
        global tot_fruit
        tot_fruit = 50
        p = threading.Thread(target=producer, name='Farmer-1')
        p.start()
        self.assertTrue(p, "Deve ser ativada pelo fato de possuir frutas ")



def producer():
    threadLock = threading.Lock()
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
            return 1

    return None

def logging_app(c,p):
    while tot_fruit > 0:
        time.sleep(1)
        logging.debug(f' Tree ({tot_fruit} fruits) - dirty basket ({dirty_basket.qsize()}) '
                      f'- Clean Basket ( {clean_basket.qsize()} ) -  '
                      f'{p.getName()} ({clean_basket.get()}) - '
                             f'{c.getName()} ({clean_basket.get()})')
        return True
    return


def consumer():
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
    unittest.main()

    threadLock = threading.Lock()
    threads = []
