def area_of_triangle(int1, int2, int3):

    s = 1/2 * (int1 + int2 + int3)

    output = (s * (s-int1) * (s-int2) * (s-int3)) ** 0.5

    return output


