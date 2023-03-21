from multiprocessing import Pool, cpu_count
import time


def factorize(number):
    factors = []
    for n in range(1, number + 1):
        if number % n == 0:
            factors.append(n)
    print(factors)
    return factors


numbers = [128, 255, 99999, 10651060]

if __name__ == "__main__":

    start_time = time.time()
    factorized = []
    for i in numbers:
        factor = factorize(i)
    factorized = factorized.append(factor)
    end_time = time.time()

    print("Sequential execution time:", end_time - start_time, "seconds")

    start_time2 = time.time()
    with Pool(cpu_count()) as p:
        factors = p.map(factorize, numbers)
        p.close()
        p.join()
    end_time2 = time.time()

    print("Parallel execution time:", end_time2 - start_time2, "seconds.", "Cores of cpu: ", cpu_count())
