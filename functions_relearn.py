# A simple example of a function:
def function_name1(pram1):
    """
    Body: Statements to execute
    """
    print(pram1)  # this will print the pram1 only
    # We can concatenate two strings together with + sign.
    # this will print the concatenated string
    print(pram1 + ', this is Python')


# function call with its name
function_name1('Hello world')


# function call without parameter will cause error
# function_name()

def function_name2(pram1='Default Value'):
    print(pram1)
    # Let's concatenate two strings together with + sign.
    print(pram1 + ', this is Python')


# Function call without the parameter
function_name2()

function_name2('Hi')  # or function_name(pram1='Hi')


# function returns the result
def my_func1(num1, num2):
    num = num1*num2
    return num
# we can write "return num1**num2" in a single line as well


# Function call
out = my_func1(2, 3)
print(out)


def my_func(num1):
    """
    These docstrings are very useful
    Jupyter has a great feature for these strings write function name, and click shift + tab my_func -- shift + tab
    You will see these docstrings
    """
    return num1**3


print(my_func(2))
