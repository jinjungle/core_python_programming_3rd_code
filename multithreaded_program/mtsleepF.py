from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)


lock = Lock()
# generator 生成器
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('remaining: %s' % (remaining or "NONE"))
    lock.release()


def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('ALL DONE at:', ctime())


if __name__ == '__main__':
    main()
