"""
    This module is a `Thermometer` which uses
two devices, one as server and one as client
to detect environmental temperature using sound
transmission speed. At a glance, we can summarize
this phenomenon into this simple equation, on
which the basis of this test is implemented:

    (1)         v = 331 * SQRT(1 + T / 273)

Which, then comes to be written in this form:

    (2*)        T =  273 * ((v/331)^2 - 1)

In this case, for evaluating the LHS of the
equation, we only need to find value of
variable (v), which can be arranged in way
of measuring the time duration between sending
and receiving of the sound wave. It is where
having two devices in same environment comes
to be useful. Using the simple motion formula

    (3)         v = x/t

We can obtain value of the LHS setting x** to 1m
and achieving t through said measurement. Thus,
putting x and t inside the equation generates
value of v, using which we can now evaluate in
formula (2) and obtain the desired environmental
temperature.



__NOTES __

(*) It is to be noted that the result is in Kelvin,
and we can generate the results in Celsius and
Fahrenheit afterward using following formulae.

    (i)         θ = T - 273
    (ii)        F = (9/5)(θ) + 32

(**) x is the distance between devices, and can be
set to desired distance in meters. Also, please note
that the second device requirement can be completely
ignored if distance to the nearest wall or obstacle
can be measured.
"""
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
