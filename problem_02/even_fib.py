import sys


def even_fib_sum(upper_bound):
    sum = 0
    fib_iterable = fib_generator()
    fib_number = fib_iterable.next()
    while fib_number <= upper_bound:
        if (not fib_number % 2):
            sum += fib_number
        fib_number = fib_iterable.next()
    return sum

def fib_generator():
    fib = 1
    next_fib = 2
    while True:
        yield fib;
        temp = fib
        fib = next_fib
        next_fib = temp + fib


if __name__ == "__main__":
    print even_fib_sum(int(sys.argv[1]))
