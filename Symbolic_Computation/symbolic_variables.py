from sympy import *

x = Symbol('x')
y = symbols('y')
z = symbols('z')

print("Output for the symbolic variables with same names : ", x + y + z)


# symblic variables with different names

a = symbols('x')
b = symbols('y')
c = symbols('z')

print("Output for the symbolic variables with different names : ", a + b + c)
