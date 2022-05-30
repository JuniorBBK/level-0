def area_of_triangle(side1, side2, side3):

    semiperimeter = 1/2 * (side1 + side2 + side3)

    area = (semiperimeter * (semiperimeter-side1) * (semiperimeter-side2) * (semiperimeter-side3)) ** 0.5

    return area
