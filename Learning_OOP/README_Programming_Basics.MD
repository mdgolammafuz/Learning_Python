# Thinking like a Computer, the logic of object oriented programming



## Understanding Objects 

1. Understanding objects in object oriented programing :

Objects can be designed to model real-world things in software.
Objects group together details.
Abstraction means showing only what’s relevant and useful for the person using it.
By hiding all the inner workings of a given object with abstraction, we are able to reduce their apparent complexity.

2. Discovering Computer's inner architect : Planning out objects

A plan or blueprint for an object is called a class.
A class defines the attributes (a description), the methods (what it does), and the access level (who can use it) for an object.
To create an object, you have to instantiate it. An instantiated object is called an instance of a class.
Objects from the same class can differ in the details if they have different values for their attributes. They still have to follow the class plan, though! 
Encapsulation is the bundling together of attributes, methods, and access control in order to protect an object. 

3. Interact with objects: complex systems and sending messages

Objects can have attributes that are objects. These objects also have their own independent blueprint (class), attributes, behaviors, and access.
Objects communicate with one another by sending messages.
Associating objects with other objects allows you to more easily adapt and make changes to your system.  



## Using logic and element of programming

1. Discovering how a computer solves a problem : Solving problems like a computer

Computers can solve problems by performing billions of operations per second.
A programmer’s job is to find solutions. They do this by breaking down problems into easy-to-follow steps for a computer.
Programming languages allow people to communicate with computers.
Computers are literal and do exactly what you tell them to.

2. Working with sequences : Understanding logic flow 

A logic flow is the order in which steps are completed in a program.
Steps are completed sequentially, not simultaneously.
Some steps are independent, which means they can be completed in any order.

3. Working with states and logical operators :

Computers use logical operations to solve problems. 
Boolean values can be either true or false.
Other values are null or empty. 
Key logical operators are NOT, AND, OR.

4. Following a sequence with conditions :

Use if/else statements for conditions.
You can compare elements using greater than, less than, and equal to.

5. Iterating the instructions by working with loops :

While loops are used when you know the end state you want, but not the number of iterations.
For loops are used when you know the exact number of iterations you need.  
An infinite loop is a while loop that gets stuck because it doesn’t have an end condition. 



# Understanding the functions

1. Understanding how functions work :

Coding is fun but you should not duplicate time and effort: use functions for repetitive tasks.
Functions contain a series of instructions you can use again and again.
Functions have names.
When you need a function, you can call it by name.  

2. Using functions : Black boxes, a everyday reality

A black box performs something useful without needing to how it does what it does.
We use black box functions regularly in real life and in programming. 

3. Writing clean functions : 4 steps of writing functions 

Writing clean functions is critical for making sure they work well.
Good function writing takes 4 basic steps:
    1. Choose a goal and name the function accordingly
    2. Define the end result
    3. Define what the function requires as input
    4. Implement the logic

4. Defining and sending messages with functions : parameters and return values 

Functions can receive messages through parameters.
Functions can send messages through return values. 



# Learning about data storage  

1. Where is the data ? variables

Variables are containers where we store data. 
Variables are stored in specific locations in computer memory. 
Variables have different types. 
Variables have names

2. Primitive datatypes : Things all computers know

All computers understand the fundamental primitive data types.
Boolean can be only true or false.
String contains a series of alphanumeric characters.
Number is used in arithmetic.
Null is the presence of nothing.

Types define what we can put in a variable. There are different types we can use. We've actually seen one of them already: objects! These are often referred to as complex types because they're complex! 🎈

    1) Boolean: As you saw previously, the Boolean data type can contain only the values true or false.  This is the only 
    data type the computer can use to make decisions.
    2) Null: Empty is not a primitive data type, but it is a value.
    2) String: The string data type is a series of characters. By characters we mean letters or letter-like symbols used to  communicate.
    3) Number: The number data type is used for arithmetic operations.  Numbers can be positive or negative and may          contain a decimal point.

3. Recognizing the array data type : 

An array is a container for other objects.
The array contains a fixed number of buckets that you specify when it is created.
Array buckets are accessed using zero-based counting.
Array processing is very fast. Array buckets can be accessed in constant time (very fast) so even if there were two-million objects inyour container, the time to fetch an objects is the same as if there were only a few objects.

4. List data types : List container

List is an ordered container of objects.
List size is dynamic and can become bigger or smaller according to your needs. 

5. Exploring the dictionary data type :

The map or dictionary data type stores rows of key/value pairs.
Rows can be added/removed for any key you wish.
Size is dynamic, and can shrink/grow in real time. 



## Summary:

    1. Identify how computers use objects in programming.
    2. Understand how computers use logic to make decisions and run programs.
    3. Explain what functions are used for in programming. 
    4. Recognize how data is stored in computer programming.





# Writing methods and classes with Python

1. Understanding Classes:

Classes are templates for objects.
Classes combine state (data or variables) and behavior (methods) that apply to that data.
An object can be passed around and used in a program

## Class
The relationship between classes and objects is like the relationship between a blueprint and a building. The blueprint defines where the walls should be, but the house is made of bricks and mortar. With a class, you can instantiate objects based on that blueprint. Those objects have the same structure.

But what’s actually in a class? A class contains state and behavior. State refers to data or variables. A Person class might have a “name” variable, for instance. A class’s behavior is simply a set of things that the class can do. This behavior is held in methods, which are identical in concept to functions.

## So what’s the difference between a method and a function?

A method is part of a class, while a function is independent of them. Methods can take parameters, modify the object's internal state, call other methods or functions, and return values. You “call” a function or method when you use it in code. For example, the line  x = add(2, 3)  calls the  add  function with the parameters 2 and 3.

Since a method is part of a class, it’s also part of an object that’s created from that class. The only difference between a function and a method is that methods are part of a class/object.

## Objects

Unlike a class, which is just a template, an object is a real thing that can be passed around and used in your program.

Objects can be stored in a variable, and the type of that variable is the class. Just like the type of the number “5” is an integer, and the type of the word “hello” is a string, the type of a customer object is Customer.

We can modify the state of an object or call methods on it.

We can instantiate multiple objects from the same class, and those objects are independent.

We can already create variables and make functions, why make classes and objects?

Object-oriented programming (OOP) is a different way of thinking about programming than the procedural programming you will have done before. OOP logically ties together data and the code that applies to that data.

2. Write a Python Class :

Make a class using the  class  keyword.
The  __init__  method is known as the constructor.
Constructors are called when an object is created.

3. Creating Python Objects : Instantiate an Object

We can instantiate objects using their class’s name.
When We instantiate an object, we’re calling its constructor, and need to provide it the right parameters.

We can access and modify attributes, and call methods, using the  object.attribute  syntax.
Python deals with that for us! Remember that  self  just refers to  this object, and Python already knows what object we’re calling the method on. 

