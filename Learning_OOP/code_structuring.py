"""
Listing the Resources Defined in a Package or Module:
You are implementing a program at work and you need to use a package that you have never interacted with before. You find that you need to write a script to list all resources that are available in that package.

Our aim here is to list the resources defined in a package or module.

Define a function called package_enumerator, which will take a package or module name and print out the names of all the resources defined in the package or module. Inside the function, use a for statement to list the package's resources.

We have provided code that passes the string module to our function. Run your script using python main.py in the terminal, the output should be as follows:

Formatter
Template
_ChainMap
_TemplateMetaclass
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_re
_string
ascii_letters
ascii_lowercase
ascii_uppercase
capwords
digits
hexdigits
octdigits
printable
punctuation
whitespace
Task

Follow the above instructions, define a function called package_enumerator, which will take a package or module name and print out the names of all the resources defined in the package or module. For this task we will test for the resources within the string module.
"""

# Define your function here
"""
if __name__ == '__main__':
    import string 
    package_enumerator(string)
"""
