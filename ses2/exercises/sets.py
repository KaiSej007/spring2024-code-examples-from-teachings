# Basic set exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# A. Create a Set
# Write a function `create_set` that takes a list of elements and returns a set containing the same elements.
# e.g. create_set([1, 2, 3, 2]) yields {1, 2, 3}
def create_set(list):
    return set(list)

# B. Set Union
# Write a function `union_sets` that takes two sets and returns their union.
# e.g. union_sets({1, 2, 3}, {3, 4, 5}) yields {1, 2, 3, 4, 5}
# Make 2 versions, one using the set method, and one using an operator.
def union_sets(s1, s2):
    return s1.union(s2)

# C. Set Intersection
# Write a function `intersect_sets` that takes two sets and returns their intersection.
# e.g. intersect_sets({1, 2, 3}, {2, 3, 4}) yields {2, 3}
# Make 2 versions, one using the set method, and one using an operator.
def intersect_sets(s1, s2):
    return s1.intersection(s2)

# D. Set Difference
# Write a function `difference_sets` that takes two sets and returns the difference (elements in the first set but not in the second).
# e.g. difference_sets({1, 2, 3}, {2, 3, 4}) yields {1}
# Make 2 versions, one using the set method, and one using an operator.
def difference_sets(s1, s2):
    return s1.difference(s2)

# E. Symmetric Difference
# Write a function `symmetric_difference_sets` that takes two sets and returns their symmetric difference (elements in either set but not in both).
# e.g. symmetric_difference_sets({1, 2, 3}, {3, 4, 5}) yields {1, 2, 4, 5}
# Make 2 versions, one using the set method, and one using an operator.
def symmetric_difference_sets(s1, s2):
    return s1.symmetric_difference(s2)

# F. Set Subset
# Write a function `is_subset` that takes two sets and returns `True` if the first set is a subset of the second set, otherwise `False`.
# e.g. is_subset({1, 2}, {1, 2, 3}) yields `True`
# Make 2 versions, one using the set method, and one using an operator.
def is_subset(s1, s2):
    return s1.issubset(s2)

# G. Set Superset
# Write a function `is_superset` that takes two sets and returns `True` if the first set is a superset of the second set, otherwise `False`.
# e.g. is_superset({1, 2, 3}, {2, 3}) yields `True`
# Make 2 versions, one using the set method, and one using an operator.
def is_superset(s1, s2):
    return s1.issuperset(s2)


# Function to test the output against the expected result
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {got} expected: {expected}')

# Calls the above functions with interesting inputs.
def main():
    print('create_set')
    test(create_set([1, 2, 3, 2]), {1, 2, 3})
    test(create_set(['abc', 'xyz', 'abc', 'xyz']), {'abc', 'xyz'})
    test(create_set([True, False, False, False, True]), {True, False})
    print()

    print('union_sets')
    test(union_sets({1, 2, 3}, {3, 4, 5}), {1, 2, 3, 4, 5})
    test(union_sets({'apple', 'banana'}, {'banana', 'cherry'}), {'apple', 'banana', 'cherry'})
    test(union_sets({'x', 'y'}, {'y', 'z', 'x'}), {'x', 'y', 'z'})
    print()

    print('intersect_sets')
    test(intersect_sets({1, 2, 3}, {2, 3, 4}), {2, 3})
    test(intersect_sets({'apple', 'banana'}, {'banana', 'cherry'}), {'banana'})
    test(intersect_sets({'x', 'y', 'z'}, {'a', 'y', 'z'}), {'y', 'z'})
    print()

    print('difference_sets')
    test(difference_sets({1, 2, 3}, {3, 4, 5}), {1, 2})
    test(difference_sets({'apple', 'banana', 'cherry'}, {'banana'}), {'apple', 'cherry'})
    test(difference_sets({'x', 'y', 'z'}, {'y', 'z'}), {'x'})
    print()

    print('symmetric_difference_sets')
    test(symmetric_difference_sets({1, 2, 3}, {3, 4, 5}), {1, 2, 4, 5})
    test(symmetric_difference_sets({'apple', 'banana'}, {'banana', 'cherry'}), {'apple', 'cherry'})
    test(symmetric_difference_sets({'x', 'y'}, {'y', 'z'}), {'x', 'z'})
    print()

    print('is_subset')
    test(is_subset({1, 2}, {1, 2, 3}), True)
    test(is_subset({'apple', 'banana'}, {'banana'}), False)
    test(is_subset({'x'}, {'x', 'y', 'z'}), True)
    print()

    print('is_superset')
    test(is_superset({1, 2, 3}, {2, 3}), True)
    test(is_superset({'banana'}, {'apple', 'banana', 'cherry'}), False)
    test(is_superset({'x', 'y', 'z'}, {'x', 'z'}), True)
    print()

main()