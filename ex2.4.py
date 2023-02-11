import json
import random
import sys
import time

import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    # Terminate the recursion if the sub-array size is small
    if high - low <= 10:
        func2(arr, low, high)
        return
    
    # Choose the pivot randomly
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]

    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    # Tail call optimization
    func1(arr, low, j - 1)
    func1(arr, j + 1, high)

def func2(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    with open('ex2.json', "r") as f:
        data = json.load(f)

    times = []
    arr_sizes = []

    for arr in data:

        start_time = time.time()
        func1(arr, 0, len(arr) - 1)
        stop_time = time.time()
        execution_time = stop_time - start_time
        arr_sizes.append(len(arr))
        times.append(execution_time)



    plt.plot(arr_sizes, times)
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Sorting Preformance")
    plt.show()
