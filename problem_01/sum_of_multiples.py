import sys


def sum_of_multiples(upper_bound, prime1, prime2):
    """
     e.g., when upper_bound=1000, prime1=3, prime2=5
     returns the sum of all the multiples of 3 or 5 below 1000.
    """
    sum = 0
    for i in range(2, upper_bound):
        if (is_multiple(i, prime1) or is_multiple(i, prime2)):
            sum += i
    return sum


def is_multiple(to_be_tested, prime):
    "test whether a number is the multiple of a prime number"
    if ((to_be_tested / prime) * prime == to_be_tested):
        return True
    else:
        return False


if __name__ == "__main__":
    print "arguments include: upper_bound-{0}, prime1-{1}, prime2-{2}".format(
          sys.argv[1], sys.argv[2], sys.argv[3])
    print sum_of_multiples(int(sys.argv[1]),
                           int(sys.argv[2]), int(sys.argv[3]))
