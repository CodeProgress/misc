import pylab

vals = []
valsMemo = []

def fib(x):
    vals.append(x)
    if x <= 1:
        return 1
    return fib(x-1) + fib(x-2)

memo = {}
def fib_with_memo(x):
    valsMemo.append(x)
    if x in memo:
        return memo[x]
    if x <= 1:
        return 1
    memo[x] = fib_with_memo(x-1) + fib_with_memo(x-2)
    return memo[x]

fib(10)
fib_with_memo(10)
pylab.plot(vals)
pylab.plot(valsMemo)
pylab.show()
