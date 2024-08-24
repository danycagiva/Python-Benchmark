#Benchmark Fibonnaci Single-Threaded
from time import perf_counter

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
if __name__ == '__main__':
    times = list()
    for _ in range(3):
        time_start = perf_counter()
        fib(40)#if you want to change the amount of numbers, change the number 40 to your desired number
        time_duration = perf_counter() - time_start
        print(f'> {time_duration:.3f} seconds')
        times.append(time_duration)
    time_average = sum(times) / 3.0
    print(f'average {time_average:.3f} seconds')
