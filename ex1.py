def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

if __name__ == "__main__":
    import timeit
    # Time func(36)
    print(timeit.timeit("func(36)", setup="from __main__ import func", number=1))
    print(func(36))