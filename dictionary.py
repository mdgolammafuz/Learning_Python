# Let's create a simple dictionary, d1.
dictionary = {'key1': 1, 'key2': True, 'key3': 'value3'}

print("Dictionary : {}".format(dictionary))
print("Dictionary:", dictionary)


dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print("Value with Key :", dictionary['key1'])

print("Value with Key : {}".format(dictionary['key1']))

# both keys, k1 and k2 have lists as their values in d2.
d2 = {'k1': [1, 2, 3], 'k2': ['a', 'b']}
print("list as Value : {}".format(d2['k1']))

# Indexing the list
print("Indexed value from List : {}".format(d2['k1'][0]))


nested_d = {'k1': {'k_in': [1, 2, 3]}}
# Printing dictionary
print("Dictionary : {}".format(nested_d))

# Printing the nested dictionary
print("Nested dictionary : {}".format(nested_d['k1']))

# Printing value from nested dictionary
print("Value from nested dictionary : {}".format(nested_d['k1']['k_in']))

# We have a dictionary
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Grabbing all the keys.
print("Keys of dictionary : {}".format(d1.keys()))  # try "list(d1.keys())"
print("Keys of dictionary :", list(d1.keys()))

# Grabbing all the values
print("Values of dictionary : {}".format(d1.values()))
print("Values of dictionary :", list(d1.values()))

# Grabbing all key-value pairs
print("Key-Value pairs of dictionary : {}".format(d1.items()))
print("Key-Value pairs of dictionary :", list(d1.items()))
