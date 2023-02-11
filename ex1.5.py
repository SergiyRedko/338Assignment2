def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# Declare dictionary to store fibonacci numbers
fib_dict = {0:0, 1:1}
def fib(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib(n-1) + fib(n-2)
        return fib_dict[n]

if __name__ == "__main__":
    import timeit
    import matplotlib.pyplot as plt
    
    slow_fib = []
    
    for i in range(0, 36):
        slow_fib.append(timeit.timeit("func({})".format(i), setup="from __main__ import func", number=1))

    fast_fib = []

    for i in range(0, 36):
        fast_fib.append(timeit.timeit("fib({})".format(i), setup="from __main__ import fib", number=1))

    # Plot slow_fib and fast_fib in plt
    plt.plot(slow_fib, label="Slow Fibonacci")
    plt.plot(fast_fib, label="Fast Fibonacci")
    plt.legend()
    plt.title("Fibonacci Time Comparison")
    plt.xlabel("nth Fibonacci Number")
    plt.ylabel("Time (s)")
    plt.show()
