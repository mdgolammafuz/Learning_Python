def square():
    # Creating an empty list
    list = []
    # Using the range method with loop
    for i in range(1, 6):
        # adding the squares of each numbers into the list
        list.append(i**2)
    # return the resultant list
    return list


print(square())
