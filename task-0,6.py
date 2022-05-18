def max_number(int1, int2, int3):

    if int1 > int2 and int2 > int3:
        output = int1 
    elif int2 > int1 and int2 > int3:
        output = int2
    else:
        output = int3

    return output 


