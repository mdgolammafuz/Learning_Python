#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[14]:


# NUMBERS :

# addition
print("Addition : ", 5 + 2)

# subtraction
print("Subtraction : ", 5 - 2)

# multiplication
print("Multiplication : ", 5 * 2)


# In[3]:


# division
print("Division : ", 5 / 2)


# In[4]:


# Power of number
print("Power of number : ", 5 ** 2)


# In[5]:


print(1 + 2 * 3 + 4)


# In[6]:


# Operator precedence
print((1 + 2) * (3 + 4))


# In[7]:


# returns 0, 6 is even no.
print(6 % 2)

# returns 1, 5 is odd no. (if we divide 5 by 2, remainder is 1)
print(5 % 2)


# In[25]:


# Let's try x = 5 and y = 3
x = 5
y = 3
print(x)
print(y)


# In[24]:


x = 5
y = 3
# Adding x and y
print(x + y)
# Multiplying x and y
print(x * y)


# In[10]:


x = 5
y = 3
# Subtraction of the variables and assignment of the result to a new variable
z = x - y        # 5 - 3
print(z)


# In[21]:


x = 5
y = 3
x = y + 2
x = x * x
print("x : ", x)


# In[12]:


name_of_the_variable = 20
print(name_of_the_variable)


# In[20]:


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


# In[19]:


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}'.format(one=name, two=number))


# In[18]:


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}, {one} again and {two} again'
      .format(one=name, two=number))


# In[26]:


# Let's create a string
X = "MAFUZ"

# grabbing the first letter in the String
print('First Letter in the String : {}'.format(X[0]))

# grabbing the last letter
print('Last Letter in the String : {}'.format(X[-1]))


# In[30]:


# IndexError exception

city = 'Boston'
print(city[6])


# In[29]:


first_name = "Golam "
last_name = "Mafuz"
# concatenation of String
full_name = first_name + last_name
print(full_name)


# In[31]:


# Assign 'Bill' to friend.
friend = 'Mafuz'
# Can we change the first character to 'J'?
friend[0] = 'J' # No, this will cause an error!


# In[ ]:




