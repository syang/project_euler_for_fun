import sys


def find_largest_prime_factor(number):
    """
    return the largest prime number that is the factore of number;
    return -1 if the number itself is a prime
    """

    start = number / 2
    factor = 1

    if (start <= 2):
        return factor

    for factor in range(start, 1, -1):
        if ((not number % factor) and is_prime(factor)):
            return factor
    return 1


def is_prime(number):
    if (number == 2 or number == 3):
        return True

    for x in range(2, number/2 + 1):
        if (not number % x):
            return False
    return True

if __name__ == "__main__":
    print find_largest_prime_factor(int(sys.argv[1]))
