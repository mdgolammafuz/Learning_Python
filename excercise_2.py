def you_pay(cost, is_monday):
    # Check the cost is less than 50
    if cost < 51:
        # Calculate the 10% discount and return the remaining cost
        return ((cost)-(cost/100)*10)
    # check if it's monday and customer is paying more than 50
    elif is_monday and cost >= 51:
        # 10 cads off
        new_cost = cost - 10
    else:
        new_cost = cost
# if cost is between 50 to 100 then calculate 20% discount and return the remaining spending
    if cost > 50 and cost <= 100:
        return (new_cost-((new_cost)/100)*20)
    else:
        # calculating 40% discount and return the remaining cost
        return (new_cost-((new_cost)/100)*40)


print(you_pay(50, True))
