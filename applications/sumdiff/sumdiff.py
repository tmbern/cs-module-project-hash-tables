"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
# this might be cheating but this is a quick way that i was able to get all possible
# combinations that we could have from a given tuple of numbers
from itertools import product

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# need to get all possible combinations of 4 numbers from a given set of numbers of any length
# as the length of the set gets large this just doesnt run... there must be a better solution than
# using the itertools...

dummy_list = list(product(q, repeat=4))

for i in dummy_list:
    a, b, c, d = f(i[0]), f(i[1]), f(i[2]), f(i[3])

    if a + b == c - d:
        print(f'{a} + {b} = {c} - {d}')


