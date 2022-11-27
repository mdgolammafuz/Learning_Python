# A simple while loop
i = 1  # initializing a variable i = 1
while i < 5:  # loop test
    # Run the block of code (given below), till "i < 5"
    # from your previous lecture, recall the placeholder in the print statement with the format() method!
    print('The value of i is: {}'.format(i))
    i = i+1  # increase i by one for each iteration


i = 1
while i < 5:
    print('The value of i is: {}'.format(i))
    i = i+1
else:
    print('Exit loop')


my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print('Hello world')


my_list = [1, 2, 3, 4, 5]
# printing the square of the numbers in my_list
for num in my_list:
    print(num**2)

# List Comprehension
# We have a list x
x = [2, 3, 4, 5]
out = []  # empty list for squares
for num in x:  # loop test
    # taking squares and appending them to the empty list "out"
    out.append(num**2)
print(out)  # using print to get the output
