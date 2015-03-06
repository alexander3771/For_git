a = [i+j for i in xrange(4) for j in xrange(5)]

print a


def fib(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a+b
        yield a

c = fib(20)

print list(c)
