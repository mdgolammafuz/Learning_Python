# Thinking like a Computer : The logic of object oriented programming


# First : Understanding Objects 

## Understanding objects in object oriented programing :

1. Objects can be designed to model real-world things in software.

2. Objects group together details.

3. Abstraction means showing only what’s relevant and useful for the person using it.

4. By hiding all the inner workings of a given object with abstraction, we are able to reduce their apparent complexity.

## Discovering Computer's inner architect - Planning out objects :

1. A plan or blueprint for an object is called a class.

2. A class defines the attributes (a description), the methods (what it does), and the access level (who can use it) for an object.

3. To create an object, you have to instantiate it. An instantiated object is called an instance of a class.

4. Objects from the same class can differ in the details if they have different values for their attributes. They still have to follow the class plan, though! 

5. Encapsulation is the bundling together of attributes, methods, and access control in order to protect an object. 

## Interact with objects - complex systems and sending messages :

1. Objects can have attributes that are objects. These objects also have their own independent blueprint (class), attributes, behaviors, and access.

2. Objects communicate with one another by sending messages.

3. Associating objects with other objects allows you to more easily adapt and make changes to your system.  


## Second : Using logic and element of programming

## Discovering how a computer solves a problem - Solving problems like a computer :

1. Computers can solve problems by performing billions of operations per second.

2. A programmer’s job is to find solutions. They do this by breaking down problems into easy-to-follow steps for a computer.

3. Programming languages allow people to communicate with computers.

4. Computers are literal and do exactly what you tell them to.

## Working with sequences - The flow of logic :

1. A logic flow is the order in which steps are completed in a program.

2. Steps are completed sequentially, not simultaneously.

3. Some steps are independent, which means they can be completed in any order.

## Working with states and logical operators :

1. Computers use logical operations to solve problems. 

2. Boolean values can be either true or false.

3. Other values are null or empty. 

4. Key logical operators are NOT, AND, OR.

## Following a sequence with conditions :

1. Use if/else statements for conditions.

2. You can compare elements using greater than, less than, and equal to.

## Iterating the instructions by working with loops :

1. While loops are used when you know the end state you want, but not the number of iterations.

2. For loops are used when you know the exact number of iterations you need.  

3. An infinite loop is a while loop that gets stuck because it doesn’t have an end condition. 


## Third : Understanding the functions

## Understanding how functions work :

1. Coding is fun but you should not duplicate time and effort: use functions for repetitive tasks.

2. Functions contain a series of instructions you can use again and again.

3. Functions have names.

4. When you need a function, you can call it by name.  

## Using functions - Black boxes, a everyday reality :

1. A black box performs something useful without needing to how it does what it does.

2. We use black box functions regularly in real life and in programming. 

## Writing clean functions - Four steps of writing functions :

Writing clean functions is critical for making sure they work well.
Good function writing takes 4 basic steps:

    1) Choose a goal and name the function accordingly

    2) Define the end result

    3) Define what the function requires as input

    4) Implement the logic


## Defining and sending messages with functions - parameters and return values :

1. Functions can receive messages through parameters.

2. Functions can send messages through return values. 


# Fourth : Learning about Data Storage  

## Where is the data ? In the Variables

1. Variables are containers where we store data. 

2. Variables are stored in specific locations in computer memory. 

3. Variables have different types. 

4. Variables have names

## Primitive datatypes - Things all computers know :

1. All computers understand the fundamental primitive data types.

2. Boolean can be only true or false.

3. String contains a series of alphanumeric characters.
Number is used in arithmetic.

4. Null is the presence of nothing.

Types define what we can put in a variable. There are different types we can use. We've actually seen one of them already: objects! These are often referred to as complex types because they're complex! 🎈

    1) Boolean: 
    As you saw previously, the Boolean data type can contain only the values true or false.  This is the only data type the computer can use to make decisions.

    2) Null: The absence of anything
    Empty is not a primitive data type, but it is a value.

    3) String: Seies of characters or symbols
    The string data type is a series of characters. By characters we mean letters or letter-like symbols used to  communicate.

    4) Number: Float or Integer
    The number data type is used for arithmetic operations.  Numbers can be positive or negative and may          contain a decimal point.


## Recognizing the array data type : 

1. An array is a container for other objects.

2. The array contains a fixed number of buckets that you specify when it is created.

3. Array buckets are accessed using zero-based counting.

4. Array processing is very fast. Array buckets can be accessed in constant time (very fast) so even if there were two-million objects inyour container, the time to fetch an objects is the same as if there were only a few objects.

## List data types - The List container :

1. List is an ordered container of objects.

2. List size is dynamic and can become bigger or smaller according to your needs. 

## Exploring the dictionary data type - The Map :

1. The map or dictionary data type stores rows of key/value pairs.

2. Rows can be added/removed for any key you wish.
Size is dynamic, and can shrink/grow in real time. 


## Summary:

    1. Identify how computers use objects in programming.

    2. Understand how computers use logic to make decisions and run programs.

    3. Explain what functions are used for in programming. 

    4. Recognize how data is stored in computer programming.




# Writing methods and classes with Python

## First : Understanding Classes

1. Classes are templates for objects.

2. Classes combine state (data or variables) and behavior (methods) that apply to that data.

3. An object can be passed around and used in a program

## Class :
The relationship between classes and objects is like the relationship between a blueprint and a building. The blueprint defines where the walls should be, but the house is made of bricks and mortar. With a class, you can instantiate objects based on that blueprint. Those objects have the same structure.

But what’s actually in a class? 

A class contains state and behavior. State refers to data or variables. A Person class might have a “name” variable, for instance. A class’s behavior is simply a set of things that the class can do. This behavior is held in methods, which are identical in concept to functions.

## So what’s the difference between a method and a function?

A method is part of a class, while a function is independent of them. Methods can take parameters, modify the object's internal state, call other methods or functions, and return values. You “call” a function or method when you use it in code. For example, the line  x = add(2, 3)  calls the  add  function with the parameters 2 and 3.

Since a method is part of a class, it’s also part of an object that’s created from that class. The only difference between a function and a method is that methods are part of a class/object.

## Objects :

Unlike a class, which is just a template, an object is a real thing that can be passed around and used in our program. Objects can be stored in a variable, and the type of that variable is the class. Just like the type of the number “5” is an integer, and the type of the word “hello” is a string, the type of a customer object is Customer. We can modify the state of an object or call methods on it.We can instantiate multiple objects from the same class, and those objects are independent.

We can already create variables and make functions, why make classes and objects?

Object-oriented programming (OOP) is a different way of thinking about programming than the procedural programming you will have done before. OOP logically ties together data and the code that applies to that data.

## Second : Writing a Python Class 

1. Make a class using the  class  keyword.

2. The  __init__  method is known as the constructor.

3. Constructors are called when an object is created.

## Third : Creating Python Objects - Instantiate an Object

1. We can instantiate objects using their class’s name.

2. When We instantiate an object, we’re calling its constructor, and need to provide it the right parameters.

3. We can access and modify attributes, and call methods, using the  object.attribute  syntax.

4. Python deals with that for us! Remember that  self  just refers to  this object, and Python already knows what object we’re calling the method on. 


## Fourth : Appyling Inheritance in Python Code

1. A class can have a parent class or superclass.

2. The class with a parent is known as a subclass or child.

3. That class inherits attributes from its parent.

4. The child class can implement extra attributes on top of that which it inherits.


Why use Inheritance?

    1) Reusability
    The simplest reason is the same reason that you write functions - reusability.

    2) Extensibility
    Inheritance also allows for extensibility - i.e., the possibility of extending a program’s functionality without having to modify existing code. 

    3) Models
    They allow developers and development teams to build conceptual models of the behaviors and data in the system