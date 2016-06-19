class Amount(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Amount(self.num + other.num)

    def __sub__(self, other):
        return Amount(abs(self.num - other.num))

    def __str__(self):
        return 'Amount {}'.format(self.num)

    def __getattr__(self, item):
        def my_print():
            setattr(self, item, item)
            print(self.__dict__[item])
        return my_print
        #print ('attribute accessed {}'.format(self.item))


a1 = Amount(50)
a2 = Amount(100)

print (a1+a2).num
print (a1-a2).num
print str(a1)
print str(a2)

a1.sachin()

print a1.__dict__


def emptyList(l):
    [l.pop(i) for i in range(len(l)-1, -1, -1)]
l =[1, 2, 3, 4]
print l
emptyList(l)
print l



def cache(f):
    cache_map = {}
    def wrapper(*args):
        if args in cache_map:
            return cache_map[args]
        ret_val = f(*args)
        cache_map[args] = ret_val
        return ret_val
    return wrapper

@cache
def fib(n):
    return n if n == 0 or n ==1 else fib(n-1)+fib(n-2)

print fib(100)