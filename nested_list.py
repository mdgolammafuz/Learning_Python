# nested list: nesting a list with in a list
nested_1 = [1, 2, 3, [4, 5, 6]]
print("List : {}".format(nested_1))

# grabbing the nested list - count the index location of nested list starting with 0
print("Nested List : {}".format(nested_1[3]))

# grabbing element from the nested list
print("Element from nested list : {}".format(nested_1[3][0]))

# another example of nested list
nested_2 = [1, 2, [3, 4, ['a', 'b']]]
print("List : {}".format(nested_2))

# grabbing the nested list - count the index location of nested list starting with 0
print("Nested List : {}".format(nested_2[2]))

# grabbing 'a' from nested_2
print("Element from nested list : {}".format(nested_2[2][2][0]))
