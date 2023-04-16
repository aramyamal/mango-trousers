#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    if n == 0:
        return 0
    elif n >= 1:
        # print(f"current: 0 \t i: 0")
        current = 1
        prev1 = 0
        prev2 = 1
        for i in range(1, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            # print(f"current: {current} \t i: {i}")
        return current
    
def fib3(n):
    if n < 0:
        return fib2(abs(n)) * (-1)**(n+1)
    else:
        return fib2(n)

def fib(n):
    if n in (0, 1):
        return 1
    if n & 1:  # if n is odd, it's faster than checking with modulo
        return fib((n+1)//2 - 1) * (2*fib((n+1)//2) - fib((n+1)//2 - 1))
    a, b = fib(n//2 - 1), fib(n//2)
    return a**2 + b**2

print(fib(100000))