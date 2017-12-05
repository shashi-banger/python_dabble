
import timerfd,os
import select

f = timerfd.create(timerfd.CLOCK_REALTIME,0)

e = select.epoll()

e.register(f)

timerfd.settime(f,0,10,0)

while True:
    events = e.poll(1)
    for fd,event_type in events:
        print "Hello World"
        os.read(f,1024)
        timerfd.settime(f,0,2,0)

