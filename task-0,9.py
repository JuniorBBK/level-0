import re
def vowels_in_string(str):
    str = str.lower()
    vowels = ["a", "e", "i", "o", "u"]
    output = "Vowels: "

    for i in set(str):
        for j in vowels:
            if i == j:
                output += f'{i}, '

    return output[:-2]

