import sys


def sum_of_multiples(upper_bound, prime1, prime2):
    """
     e.g., when upper_bound=1000, prime1=3, prime2=5
     returns the sum of all the multiples of 3 or 5 below 1000.
    """
    sum = 0
    for i in range(2, upper_bound):
        if ((i % prime1 == 0) or (i % prime2 == 0)):
            sum += i
    return sum


if __name__ == "__main__":
    print "arguments include: upper_bound-{0}, prime1-{1}, prime2-{2}".format(
          sys.argv[1], sys.argv[2], sys.argv[3])
    print sum_of_multiples(int(sys.argv[1]),
                           int(sys.argv[2]), int(sys.argv[3]))
