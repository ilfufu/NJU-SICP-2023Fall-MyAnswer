def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1

def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    i = 1
    temp = 1
    while i <= n:
        temp *= i
        i += 1
    return temp


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    "*** YOUR CODE HERE ***"
    d = a > 0 and b > 0 and c > 0
    e = a + b > c and b + a > c and a + c > b
    return d and e

def number_of_nine(n):
    """Return the number of 9 in each digit of a positive integer n.

    >>> number_of_nine(999)
    3
    >>> number_of_nine(9876543)
    1
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n >= 10:
        if n % 10 == 9:
            i += 1
        n /= 10
        n = n // 1
    if n == 9:
        i += 1
    return i


def min_digit(x):
    """Return the min digit of x.

    >>> min_digit(10)
    0
    >>> min_digit(4224)
    2
    >>> min_digit(1234567890)
    0
    >>> # make sure that you are using return rather than print
    >>> a = min_digit(123)
    >>> a
    1
    """
    "*** YOUR CODE HERE ***"
    i = 9
    while x >= 10:
        if x % 10 < i:
            i = x % 10
        i1 = x % 10
        x = (x - i1) // 10
    if x < i:
        i = x
    return i
