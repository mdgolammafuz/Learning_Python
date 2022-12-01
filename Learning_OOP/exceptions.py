"""
An exception is raised (or thrown) when a problem occurs in a program.

You can handle exceptions using try blocks.

Exceptions are just objects, which means you can define your own custom ones!
"""

# Raising Exceptions


def half_even_number(n):
    if (n % 2 == 0):
        return n/2
    else:
        raise Exception(
            "This Function only supports halving even numbers. Received: {}".format(n))


print(half_even_number(1))


# Handling Exceptions

class TextContactSystem(ContactSystem):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        send_text_message(self.phone_number, message)


def percent_increase(initial_value, after_value):
    try:
        return (after_value/initial_value)*100
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print("Uh oh, unexpected error occurred!")
        raise e


# Writing Custom Exceptions

class InvalidEmailException(Exception):
    pass


 


class EmailContactSystem(ContactSystem):
    def __init__(self, email_address):
        if (not validate_email(email_address)):
            raise InvalidEmailException(“Invalid email address: {}”.format(email_address)
        self.email_address=email_address
