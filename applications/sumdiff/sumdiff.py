"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
# this might be cheating but this is a quick way that i was able to get all possible
# combinations that we could have from a given tuple of numbers
from itertools import product, combinations_with_replacement

# q = set(range(1, 10))
q = set(range(1, 100))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# need to store all possible results of the function for each value in q
cache = {}
for i in q:
    cache[i] = f(i)



# need to get all possible combinations of 4 numbers from a given set of numbers of any length
# as the length of the set gets large this just doesnt run... there must be a better solution than
# using the itertools...

# dummy_list = list(product(q, repeat=4))
nums = product(q, repeat=4)

# def sumdiff(range_of_numbers):
#     for i in range_of_numbers:
#         a, b, c, d = f(i[0]), f(i[1]), f(i[2]), f(i[3])

#         if a + b == c - d:
#             print(f'{a} + {b} = {c} - {d}')

# create new cache to only store values where  a + b = c - d
cache_v2 = {}

# refactored above code to utilize a cache
def sumdiff(combinations_of_nums):
    for i in combinations_of_nums:
        a, b, c, d = i[0], i[1], i[2], i[3]

        if cache[a] + cache[b] == cache[c] - cache[d]:
            cache_v2[i] = f'{cache[a]} + {cache[b]} = {cache[c]} - {cache[d]}'
            # print(f'{cache[a]} + {cache[b]} = {cache[c]} - {cache[d]}')

    return cache_v2

print('done')

if __name__ == "__main__":
    results = sumdiff(nums)
    for k, v in results.items():
        print(k, v)