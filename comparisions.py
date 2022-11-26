print('3 > 4 : ', 3 > 4)  # 3 greater than 4?

print('3 < 4 : ', 3 < 4)  # 3 less than 4?

print('2 >= 2 : ', 2 >= 2)  # 2 greater or equal to 2?

print('3 <= 4 : ', 3 <= 4)  # 3 less or equal to 4?

# == is different than =, which is assignment operator
print('1 == 1 : ', 1 == 1)

# We can compare strings using == operator
print("'Tom' == 'TOM' : ", 'Tom' == 'TOM')
print("'Tom' == 'Jim' : ", 'Tom' == 'Jim')
print("'Tom' == 'Tom' : ", 'Tom' == 'Tom')
# Not equal
print("'Tom' != 'Tom' : ", 'Tom' != 'Tom')

# "and" operator
print("(1 < 2) and (2 < 3) : ", (1 < 2) and (2 < 3))
# parentheses are there to make the statement more readable

# "or" operator
print("(1 < 2) or (2 > 3) : ", (1 < 2) or (2 > 3))
print("(1>2)or(2>3) : ", (1 > 2) or (2 > 3))

# Multiple operators
print("(1 == 2) or (2 == 3) or (4 == 4) : ", (1 == 2) or (2 == 3) or (4 == 4))

# Let’s say we have the following condition
if 3 > 2:
    print('True')
# print statement will only execute if the condition is satisfied
# Notice that with print statement, we will not see typical output cell [some_number]

if 3 == 2:  # You can change == to != to print True
    print('True')
else:
    print('False')
