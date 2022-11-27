
print("Hello, World!")

# NUMBERS :

# addition
print("Addition : ", 5 + 2)

# subtraction
print("Subtraction : ", 5 - 2)

# multiplication
print("Multiplication : ", 5 * 2)

# division
print("Division : ", 5 / 2)


# Power of number
print("Power of number : ", 5 ** 2)


print(1 + 2 * 3 + 4)


# Operator precedence
print((1 + 2) * (3 + 4))


# returns 0, 6 is even no.
print(6 % 2)

# returns 1, 5 is odd no. (if we divide 5 by 2, remainder is 1)
print(5 % 2)


# Let's try x = 5 and y = 3
x = 5
y = 3
print(x)
print(y)


x = 5
y = 3
# Adding x and y
print(x + y)
# Multiplying x and y
print(x * y)


x = 5
y = 3
# Subtraction of the variables and assignment of the result to a new variable
z = x - y        # 5 - 3
print(z)


x = 5
y = 3
x = y + 2
x = x * x
print("x : ", x)


name_of_the_variable = 20
print(name_of_the_variable)


# STRINGS :

# creating single quotes string
string_example = 'creating single quotes string'

# creating double quotes string
string_example_2 = "creating double quotes string"

# we have lots of other quotes, let's wrap them in double quotes
string_example_3 = "we have lots of other quotes, let's wrap them in double quotes"

print(string_example)
print(string_example_2)
print(string_example_3)


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}'.format(one=name, two=number))


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}, {one} again and {two} again'
      .format(one=name, two=number))


# Let's create a string
X = "MAFUZ"

# grabbing the first letter in the String
print('First Letter in the String : {}'.format(X[0]))

# grabbing the last letter
print('Last Letter in the String : {}'.format(X[-1]))


# IndexError exception

# city = 'Burdwan'
# print(city[7])


first_name = "Golam "
last_name = "Mafuz"
# concatenation of String
full_name = first_name + last_name
print(full_name)


# Assign 'Mafuz' to friend.
friend = 'Mafuz'
# Can we change the first character to 'J'?
# friend[0] = 'J'  # No, this will cause an error!
