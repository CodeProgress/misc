from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f

@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

memo = {}

@trace
def fibWithMemo(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n in memo: 
            return memo[n]
        else:
            memo[n] = fibWithMemo(n-1) + fibWithMemo(n-2)
            return memo[n]

fib(7)
print '---------------------------'
fibWithMemo(7)

# Adapted from course "Design of Computer Programs"

