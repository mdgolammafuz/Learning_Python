# program to quit from python interactive cell to terminal
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
