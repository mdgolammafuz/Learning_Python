# A list of numbers
list_of_numbers = [4, 5, 6]
# We can have a list of stings 'd', 'e', 'f' -- Note strings are in quotes
list_of_string = ['d', 'e', 'f']

print("List of Numbers : {}".format(list_of_numbers))
print("List of Strings : {}".format(list_of_string))

# We can assign a list to a variable "my_list".
my_list = ['d', 'e', 'f']
print("List : {}".format(my_list))

# appending a value to list
my_list.append('g')
print("List after appending : {}".format(my_list))


# pop method
print("Item by pop method : {}".format(my_list.pop()))

my_list = ['d', 'e', 'f']

# grab the first item in the list
print("First element in the List : {}".format(my_list[0]))

# grab everything after first element
print("Everything after first element : {}".format(my_list[1:]))

# grab a slice from index location 1 to 2, but not including the element at index 3
print("A slice from index location 1 to 2: {}".format(my_list[1:3]))


# Lists are mutable
my_list = ['d', 'e', 'f']
# pass in the element 'hi' to the index 0
my_list[0] = 'hi'
print("List : {}".format(my_list))
