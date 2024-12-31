from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
import time

def quicksort_parallel(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2]
        less = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        greater = [x for x in data if x > pivot]

        return quicksort_parallel(less) + equal + quicksort_parallel(greater)

def parallel_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    parts = partition(data, pivot)
    pool = Pool()
    parts = pool.map(quicksort_parallel, parts)
    pool.close()
    pool.join()
    return merge(parts)

def partition(data, pivot):
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return [less, equal, greater]
def merge(sorted_parts):
    return sum(sorted_parts, [])

if __name__ == '__main__':
    data_sizes = [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]
    times_parallel = []

    for size in data_sizes:
        data = np.random.randint(1, 1000000, size)
        start_time = time.time()
        sorted_data = parallel_sort(data)
        end_time = time.time()
        times_parallel.append(end_time - start_time)

    plt.plot(data_sizes, times_parallel, marker='o')
    plt.xlabel('Data Size')
    plt.ylabel('Time (s)')
    plt.title('Parallel Quicksort Performance')
    plt.grid(True)
    plt.show()