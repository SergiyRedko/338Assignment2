# Declare dictionary to store fibonacci numbers
fib_dict = {0:0, 1:1}
def fib(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib(n-1) + fib(n-2)
        return fib_dict[n]

if __name__ == "__main__":
    print(fib(35))
    print(fib_dict)