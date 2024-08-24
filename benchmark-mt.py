#Benchmark with Fibonnaci Multi-Threaded

from time import perf_counter
from multiprocessing import Pool, cpu_count

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
if __name__ == '__main__':
    times = list()
    p = Pool(processes=cpu_count())
    for _ in range(3):
        time_start = perf_counter()
        p.map(fib, [40] * cpu_count())#if you want to change the amount of numbers, change the number 40 to your desired number
        time_duration = perf_counter() - time_start
        print(f'> {time_duration:.3f} seconds')
        times.append(time_duration)
    p.close()
    p.join()
    time_average = sum(times) / 3.0
    print(f'average {time_average:.3f} seconds')
