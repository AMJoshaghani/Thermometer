from server import emit
from client import listen
from worker import Worker
from multiprocessing import Process, Manager

dX = 1  # This can be changed accordingly

if __name__ == '__main__':
    manager = Manager()
    res = manager.dict()

    p1 = Process(target=emit, args=(res,))
    p1.start()
    p2 = Process(target=listen, args=(res,))
    p2.start()
    p1.join()
    p2.join()
    if res['ok']:
        w = Worker(dt=res['∆t'], dx=dX)
        w.evaluate_temperature()
        print(w.temperature(unit='C'), "^C")
    else:
        print(res['e'])
