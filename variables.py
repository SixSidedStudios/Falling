from threading import Timer

def timeout():
    print 'Too slow!'

t = Timer(5000, timeout)
