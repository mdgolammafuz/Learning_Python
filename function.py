# 1. Function which performs a task
def greet(name):
    print(f"Hello {name}!")
    print("You are welcome.")


greet("Mafuz")

# will print none as the function returns an absense of value
print(greet("Mafuz"))


# 2. Function which returns a value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mafuz")
file = open("content.txt", "w")
file.write(message)


def required_optional(x, y=10):
    return x + y


def f():
    pass
