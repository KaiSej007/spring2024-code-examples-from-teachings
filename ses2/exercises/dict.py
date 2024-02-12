# Basic dictionary exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# A. Create a Dictionary
# Write a function `create_dict` that takes two lists of the same length and returns a dictionary
# where the elements of the first list are the keys, and the elements of the second list are the values.
# e.g. create_dict(['a', 'b', 'c'], [1, 2, 3]) yields {'a': 1, 'b': 2, 'c': 3}
def create_dict(keys, values):
    return dict(zip(keys, values))

# B. Merge Dictionaries
# Write a function `merge_dicts` that takes two dictionaries and merges them into one.
# If there are overlapping keys, the values from the second dictionary should be used.
# e.g. merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) yields {'a': 1, 'b': 3, 'c': 4}
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

# C. Get Value
# Write a function `get_value` that takes a dictionary and a key, and returns the value associated with that key.
# If the key is not in the dictionary, return 'Key not found'.
# e.g. get_value({'a': 1, 'b': 2}, 'b') yields 2
def get_value(my_dict, key):
    return my_dict.get(key, 'Key not found')

# D. Key Exists
# Write a function `key_exists` that takes a dictionary and a key, and returns True if the key exists in the dictionary, otherwise False.
# e.g. key_exists({'a': 1, 'b': 2}, 'c') yields False
def key_exists(dict, key):

    return key in dict

# E. Update Value
# Write a function `update_value` that takes a dictionary, a key, and a value.
# Update the value associated with the key in the dictionary, or add the key-value pair if the key does not exist.
# Return the updated dictionary.
# e.g. update_value({'a': 1, 'b': 2}, 'b', 3) yields {'a': 1, 'b': 3}
def update_value(dict, key, value):
    dict.update({key: value})
    return dict

# F. Remove Key
# Write a function `remove_key` that takes a dictionary and a key, and removes the key from the dictionary.
# If the key is not in the dictionary, return the original dictionary.
# e.g. remove_key({'a': 1, 'b': 2}, 'a') yields {'b': 2}
def remove_key(dict, key):
    dict.pop(key, None)
    return dict

# G. Convert to List
# Write a function `dict_to_list` that takes a dictionary and returns a list of tuples,
# where each tuple is a key-value pair from the dictionary.
# e.g. dict_to_list({'a': 1, 'b': 2}) yields [('a', 1), ('b', 2)]
def dict_to_list(dict):
    return list(dict.items())

# Function to test the output against the expected result
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {got} expected: {expected}')

# Calls the above functions with interesting inputs.
def main():
    print('create_dict')
    test(create_dict(['a', 'b', 'c'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})
    test(create_dict(['x', 'y', 'z'], ['cat', 'dog', 'bird']), {'x': 'cat', 'y': 'dog', 'z': 'bird'})
    test(create_dict([1, 2, 3], ['one', 'two', 'three']), {1: 'one', 2: 'two', 3: 'three'})
    print()

    print('merge_dicts')
    test(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})
    test(merge_dicts({'x': 'cat', 'y': 'dog'}, {'y': 'parrot', 'z': 'fish'}), {'x': 'cat', 'y': 'parrot', 'z': 'fish'})
    test(merge_dicts({1: 'one', 2: 'two'}, {3: 'three', 4: 'four'}), {1: 'one', 2: 'two', 3: 'three', 4: 'four'})
    print()

    print('get_value')
    test(get_value({'a': 1, 'b': 2}, 'b'), 2)
    test(get_value({'x': 'cat', 'y': 'dog'}, 'z'), 'Key not found')
    test(get_value({1: 'one', 2: 'two'}, 1), 'one')
    print()

    print('key_exists')
    test(key_exists({'a': 1, 'b': 2}, 'c'), False)
    test(key_exists({'x': 'cat', 'y': 'dog'}, 'x'), True)
    test(key_exists({1: 'one', 2: 'two'}, 3), False)
    print()

    print('update_value')
    test(update_value({'a': 1, 'b': 2}, 'b', 3), {'a': 1, 'b': 3})
    test(update_value({'x': 'cat', 'y': 'dog'}, 'y', 'parrot'), {'x': 'cat', 'y': 'parrot'})
    test(update_value({1: 'one', 2: 'two'}, 3, 'three'), {1: 'one', 2: 'two', 3: 'three'})
    print()

    print('remove_key')
    test(remove_key({'a': 1, 'b': 2}, 'a'), {'b': 2})
    test(remove_key({'x': 'cat', 'y': 'dog'}, 'z'), {'x': 'cat', 'y': 'dog'})
    test(remove_key({1: 'one', 2: 'two'}, 1), {2: 'two'})
    print()

    print('dict_to_list')
    test(dict_to_list({'a': 1, 'b': 2}), [('a', 1), ('b', 2)])
    test(dict_to_list({'x': 'cat', 'y': 'dog'}), [('x', 'cat'), ('y', 'dog')])
    test(dict_to_list({1: 'one', 2: 'two'}), [(1, 'one'), (2, 'two')])
    print()

main()
