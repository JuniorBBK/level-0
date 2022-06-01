def max_number(num1, num2, num3):

    if num1 >= num2 and num1 > num3:
        output = num1 
    elif num2 > num1 and num2 > num3:
        output = num2
    else:
        output = num3

    return output 

