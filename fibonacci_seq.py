import itertools
def gen_fib():
    a=1
    b=1

    while(True):
        yield a
        t=b
        b=a+b
        a=t

def gen_fib_indices():
    index = 0
    for i in gen_fib():
        yield index
        index = index+i

def gen_fib_indices_1():
    a =0
    b=1
    index = 0
    while(True):
        yield index
        t=b
        b=a+b
        a=t
        index = index + a

print 'hello'
for i in gen_fib_indices():
    print i
    if i > 250:
        break


f_i=list(itertools.takewhile(lambda (i): i < 1, (gen_fib_indices_1())))
print f_i
