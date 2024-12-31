import numpy as np
import matplotlib.pyplot as plt
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

data_sizes = [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]
times = []

for size in data_sizes:
    data = np.random.randint(1, 1000000, size)
    start_time = time.time()
    sorted_data = quicksort(data)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(data_sizes, times, marker='o')
plt.xlabel('Data Size')
plt.ylabel('Time (s)')
plt.title('Serial Quicksort Performance')
plt.grid(True)
plt.show()