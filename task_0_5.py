def area_of_triangle(int1, int2, int3):

    semiperimeter = 1/2 * (int1 + int2 + int3)

    output = (semiperimeter * (semiperimeter-int1) * (semiperimeter-int2) * (semiperimeter-int3)) ** 0.5

    return output


